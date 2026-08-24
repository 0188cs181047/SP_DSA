"""
Deep Agent Orchestrator - Plan + Delegate + Collect   (Topic: Deep Agents)

Problem:
Demonstrate, with no external dependencies, the actual mechanism behind
Fig. 1 in interview_qa.md: an orchestrator that (1) turns a goal into an
explicit plan (a todo list), (2) delegates each plan step to the right
isolated sub-agent, (3) receives back only a condensed result from each
sub-agent -- never its intermediate steps, and (4) keeps looping until the
plan is fully checked off, at which point it assembles the final output.
A real deep agent's sub-agents are themselves full ReAct loops (reason,
call tools, observe, repeat) driven by an LLM; this toy version replaces
each sub-agent's internals with a deterministic, canned summary, so the
orchestration/delegation loop itself -- the actual subject of this topic --
is easy to trace by hand while debugging.

Approach:
- Represent the plan as an ordered list of step dicts (build_plan), each
  with an `id`, a `type` used to route it to the right sub-agent, a
  human-readable `detail`, and a `done`/`result` pair the orchestrator
  fills in as it works -- the todo list described in the Overview and
  question M1 (explicit planning).
- Each sub-agent (research_subagent, coder_subagent) is a plain function
  that takes a text spec and returns ONE condensed string. In a real system
  each of these would be its own LLM-driven ReAct loop with many internal
  tool calls; the orchestrator is designed to never see any of that detail
  (see M2 and Practical P1), only the final condensed line -- so from the
  orchestrator's point of view it does not matter whether the function body
  is a few lines of string formatting (as here) or a full agentic loop
  burning thousands of tokens (as in production).
- is_plan_complete is the orchestrator's stopping condition (see M6): once
  every step is marked done, the run loop stops instead of continuing
  indefinitely.
- run_orchestrator builds the plan, walks it in order (see Practical P3 for
  why that's a simplification), dispatches each pending step through the
  SUBAGENTS registry, records the condensed result, marks the step done,
  and prints a trace line -- mirroring the diagram's "condensed result ->
  orchestrator -> check off plan" cycle. Once every step is done it stitches
  the condensed results into one final combined answer.

Time Complexity:  O(steps) sub-agent dispatches, each doing O(1) (constant,
                   canned) work here; a real sub-agent's own internal ReAct
                   loop would dominate actual runtime in practice.
Space Complexity: O(steps) to hold the plan and each step's condensed
                   result -- the whole point of condensing is that this
                   stays small even if a real sub-agent internally processed
                   megabytes of tool output no one ever adds to the
                   orchestrator's own state.
"""

from typing import Callable, Dict, List


# ---------------------------------------------------------------------------
# Sub-agents: each returns ONLY a condensed one-line string (see M2, P1).
# A real implementation would run a full ReAct loop internally here instead.
# ---------------------------------------------------------------------------

_RESEARCH_FACTS = {
    "eiffel tower": (
        "Built 1887-1889 by Gustave Eiffel's company as the entrance arch "
        "for the 1889 World's Fair; originally meant as a temporary "
        "20-year structure, kept afterward because it proved useful as a "
        "radio tower."
    ),
    "python programming language": (
        "Created by Guido van Rossum, first released in 1991; designed for "
        "readability, now one of the most widely used general-purpose "
        "languages, especially in data science and AI tooling."
    ),
}


def research_subagent(topic: str) -> str:
    """Simulates an isolated sub-agent run. Internally, a real research
    sub-agent would be a full ReAct/LLM loop -- search, read, re-search,
    reason -- across many steps; here it just returns a condensed result,
    which is the whole point: the orchestrator never sees its intermediate
    steps, only this one summary line (see M2 and Practical P1)."""
    normalized = topic.strip().lower()
    for key, fact in _RESEARCH_FACTS.items():
        if key in normalized:
            return f"[research] {fact}"
    return (
        f"[research] (toy stand-in) no canned facts for '{topic}'; "
        f"a real sub-agent would search the web here."
    )


def coder_subagent(spec: str) -> str:
    """Simulates an isolated coding/writing sub-agent. A real one would
    write code, run it, read errors, and fix them across many internal
    steps (its own ReAct loop); here it just returns a condensed
    description of the 'finished' artifact. Note this does NOT look at
    research_subagent's output at all -- see Practical P4 for how you'd
    thread a shared context through so it could."""
    word_count = len(spec.split())
    return f"[code] Wrote a short write-up ({word_count}-word spec) covering: {spec}"


SUBAGENTS: Dict[str, Callable[[str], str]] = {
    "research": research_subagent,
    "code": coder_subagent,
}


# ---------------------------------------------------------------------------
# Planning: stand-in for an LLM planning call (see M1, Practical P2).
# ---------------------------------------------------------------------------

def build_plan(goal: str) -> List[dict]:
    """Stand-in for an LLM planning call: breaks the goal into an ordered
    todo list. Deliberately hardcoded to always emit the same two-step
    shape (research, then write up) regardless of what the goal actually
    says -- a real planner would vary both the NUMBER and the type of steps
    based on the goal's content (see Practical P2). Each step is a small
    dict of structured state, not a plain string (see Practical P6)."""
    return [
        {"id": 1, "type": "research", "detail": goal, "done": False, "result": None},
        {"id": 2, "type": "code", "detail": f"summary of {goal}", "done": False, "result": None},
    ]


def is_plan_complete(plan: List[dict]) -> bool:
    """The orchestrator's stopping condition: stop looping once every step
    is checked off (see M6 -- how a deep agent knows its overall task,
    not just one sub-task, is actually done)."""
    return all(step["done"] for step in plan)


# ---------------------------------------------------------------------------
# Orchestrator: walks the plan, delegates, collects, loops until done.
# ---------------------------------------------------------------------------

def run_orchestrator(goal: str) -> str:
    plan = build_plan(goal)

    print(f"Goal: {goal}\n")
    print("Plan:")
    for step in plan:
        print(f"  [{step['id']}] ({step['type']}) {step['detail']}")

    print("\nDelegation trace:")
    while not is_plan_complete(plan):
        for step in plan:
            if step["done"]:
                continue
            subagent = SUBAGENTS[step["type"]]
            result = subagent(step["detail"])
            step["result"] = result
            step["done"] = True
            print(f"  step {step['id']} ({step['type']}) -> {result}")

    final_output = "\n".join(step["result"] for step in plan)
    print("\nFinal output:")
    return final_output


if __name__ == "__main__":
    print(run_orchestrator("the history of the Eiffel Tower"))
