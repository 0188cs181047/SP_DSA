"""
ReAct Agent Loop - Simulated LLM, Real Think-Act-Observe Control Flow   (Topic: Agentic AI)

Problem:
Demonstrate, with no external dependencies and no real LLM/API calls, the
actual control-flow mechanism behind the ReAct diagram in interview_qa.md:
Thought -> Action (tool call) -> Observation, fed back into the next
Thought, looping until a Final Answer is produced or a step budget runs out.

Approach:
- `fake_llm_reason` stands in for a real LLM call. A real implementation
  would send `question` + `scratchpad` to a model and let it freely decide
  the next Thought/Action/Final Answer; this toy version uses a couple of
  hardcoded rules (extract an arithmetic expression on the first step, then
  read the last Observation back and stop) so the loop's shape is easy to
  trace by hand instead of hiding it behind a real model call.
- `parse_action` regex-extracts a structured "Action: tool[input]" or
  "Final Answer: ..." instruction out of the LLM's free-text output -- the
  same brittle text-parsing a pre-function-calling-era agent had to do
  (see Q P3 on why native structured function calling replaced this).
- `run_agent` is the actual ReAct loop: call the (fake) LLM, parse its
  output, either execute a tool and append an Observation to the scratchpad
  and repeat, or return the Final Answer -- bounded by `max_steps` so a
  reasoning step that never produces a Final Answer can't loop forever
  (see Q P2).

Time Complexity:  O(max_steps) LLM/tool calls in the worst case; each step's
                   regex parse and tool execution is O(len(text)).
Space Complexity: O(max_steps) -- the scratchpad grows by one Thought/
                   Action/Observation block per step (see Q P5 on why an
                   unbounded scratchpad eventually becomes a problem).
"""

import re


def calculator(expression: str):
    # NOTE: eval() on arbitrary input is unsafe outside a tightly controlled
    # sandbox -- restricting builtins to {} only blocks __import__/open/exec
    # etc, it is not a full sandbox. See Q P1 for what production needs instead.
    return eval(expression, {"__builtins__": {}}, {})


# A real deployment would register many tools here; see Q P4 for what
# changes once fake_llm_reason has to choose among more than one.
TOOLS = {"calculator": calculator}

EXPRESSION_RE = re.compile(r"[\d][\d\s.+\-*/()]*[\d)]")
ACTION_RE = re.compile(r"Action:\s*(\w+)\[(.*?)\]")
FINAL_RE = re.compile(r"Final Answer:\s*(.*)")


def fake_llm_reason(question: str, scratchpad: str) -> str:
    """Stand-in for a real LLM call: looks at `question` + `scratchpad` and
    decides the next Thought/Action, or a Final Answer. Simulated with two
    hardcoded rules instead of a real model so the ReAct loop's shape stays
    explicit and traceable."""
    if "Observation:" not in scratchpad:
        match = EXPRESSION_RE.search(question)
        expression = match.group(0).strip() if match else "0"
        return (
            "Thought: I need to compute the arithmetic expression in the question.\n"
            f"Action: calculator[{expression}]"
        )
    # an Observation is already in the scratchpad -- read its value back and stop
    last_line = scratchpad.strip().splitlines()[-1]
    value = last_line.split(":", 1)[-1].strip() if ":" in last_line else last_line
    return (
        "Thought: I now have the result from the tool, so I can answer.\n"
        f"Final Answer: {value}"
    )


def parse_action(llm_output: str):
    """Extract a ("final", answer) or ("action", tool_name, tool_input) tuple
    out of the LLM's raw text, or ("none", None) if neither pattern matches --
    see Q P3 for why this text-parsing approach is fragile."""
    final_match = FINAL_RE.search(llm_output)
    if final_match:
        return ("final", final_match.group(1).strip())

    action_match = ACTION_RE.search(llm_output)
    if action_match:
        tool_name, tool_input = action_match.group(1), action_match.group(2)
        return ("action", tool_name, tool_input)

    return ("none", None)


def run_agent(question: str, max_steps: int = 5) -> str:
    """The ReAct loop: reason, act, observe, repeat -- until a Final Answer
    or max_steps is reached (see Q P2 on why that guard matters)."""
    scratchpad = ""

    for step in range(1, max_steps + 1):
        llm_output = fake_llm_reason(question, scratchpad)
        print(f"--- Step {step} ---\n{llm_output}")
        scratchpad += llm_output + "\n"

        parsed = parse_action(llm_output)

        if parsed[0] == "final":
            return parsed[1]

        if parsed[0] == "action":
            tool_name, tool_input = parsed[1], parsed[2]
            if tool_name not in TOOLS:
                # see Q P6: a bad tool name becomes a visible Observation,
                # not a crash
                observation = f"Observation: Error: unknown tool '{tool_name}'"
            else:
                try:
                    result = TOOLS[tool_name](tool_input)
                    observation = f"Observation: {result}"
                except Exception as exc:
                    observation = f"Observation: Error executing {tool_name}: {exc}"
        else:
            observation = "Observation: (no Action or Final Answer found in LLM output)"

        print(observation)
        scratchpad += observation + "\n"

    return f"Agent stopped after {max_steps} steps without a Final Answer."


if __name__ == "__main__":
    print("=== Query: What is 15 * 23? ===")
    answer = run_agent("What is 15 * 23?")
    print(f"\nFinal answer returned: {answer}\n")

    print("=== Query: What is 100 / 4 + 6? ===")
    answer = run_agent("What is 100 / 4 + 6?")
    print(f"\nFinal answer returned: {answer}\n")

    print("=== Query with max_steps=1 (forces early stop before a Final Answer) ===")
    answer = run_agent("What is 9 + 9?", max_steps=1)
    print(f"\nFinal answer returned: {answer}")
