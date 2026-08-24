"""
Stateful Agent Loop with LangGraph - Real Library, Simulated "LLM"   (Topic: LangGraph)

Problem:
Unlike most other topics in this repo, LangGraph is a real, installable
library - so the point here isn't to reimplement it from scratch, it's to
show the actual mechanism behind the diagram in interview_qa.md using the
real `langgraph` package: an agent node that decides whether to call a
tool, a tools node that executes it and feeds the result back into shared
state, and a conditional edge that loops agent <-> tools until the agent
is ready to answer, then routes to END.

Only the "LLM" reasoning step is faked - fake_llm_decide() is a plain
deterministic Python function, not a real model call - so this script
runs with no API key and no internet connection. Everything else
(StateGraph, add_conditional_edges, the compiled graph's invoke() loop)
is the real langgraph library doing real work, not a simulation of it.

Example:
    Input:  {"question": "What is 12 * 7?", "steps": [], "tool_result": None, "answer": ""}
    Output: trace of 3 node visits (agent -> tools -> agent), then
            answer = "The answer is 84."

Approach:
- Define a typed AgentState (question, steps, tool_result, answer) - this
  is the object LangGraph actually threads through every node and
  checkpoints between steps in a real deployment.
- fake_llm_decide stands in for `response = model.invoke(state["question"])`:
  on the first visit tool_result is still None, so it "decides" it needs
  the calculator tool and leaves answer empty; once tool_result has been
  filled in by the tool node, it "decides" it has enough to answer.
- calculator_tool simulates executing a tool call: computes 12 * 7, writes
  the result into state, and appends a trace line - standing in for
  whatever a real @tool-decorated function or ToolNode would do.
- needs_tool is the conditional-edge routing function LangGraph calls
  after "agent" every time: "tools" while answer is still "", "end" once
  fake_llm_decide has filled it in.
- build_graph wires it together: StateGraph(AgentState) -> add_node for
  each function -> set_entry_point("agent") -> add_conditional_edges from
  "agent" using needs_tool -> a fixed add_edge("tools", "agent") to close
  the loop -> compile() into a runnable app.

Time Complexity:  O(k) node visits for k agent/tool think-act cycles; this
                   example always resolves in exactly one tool call, so 3
                   node visits total (agent, tools, agent).
Space Complexity: O(k) for the state's `steps` trace list, which grows by
                   one entry per node visited.
"""

try:
    from langgraph.graph import StateGraph, END
except ImportError:
    print("This example needs the 'langgraph' package, which is not installed.")
    print("Install it with:  pip install langgraph")
    raise SystemExit(0)

from typing import TypedDict, List, Optional


class AgentState(TypedDict):
    question: str
    steps: List[str]
    tool_result: Optional[int]
    answer: str


def fake_llm_decide(state: AgentState) -> AgentState:
    """Stand-in for a real LLM call.
    Real code:      response = model.invoke(state["question"])
    Simulated here: asks for the calculator tool on the first pass
    (tool_result is still None), and answers once a result is available.
    """
    state = dict(state)
    if state["tool_result"] is None:
        state["steps"] = state["steps"] + [
            f"Agent: I need the calculator tool for '{state['question']}'"
        ]
        # answer is left as "" -> needs_tool() will route to "tools"
    else:
        state["steps"] = state["steps"] + [
            f"Agent: I now know the result is {state['tool_result']}."
        ]
        state["answer"] = f"The answer is {state['tool_result']}."
    return state


def calculator_tool(state: AgentState) -> AgentState:
    """Simulates executing a tool call: computes 12 * 7 and writes the
    result back into shared state, exactly as a real tool node's return
    value is merged back into state for the agent node to read next."""
    state = dict(state)
    result = 12 * 7
    state["tool_result"] = result
    state["steps"] = state["steps"] + [f"Tool (calculator): 12 * 7 = {result}"]
    return state


def needs_tool(state: AgentState) -> str:
    """The conditional-edge routing function. LangGraph calls this after
    every visit to "agent" and sends execution to whichever node the
    returned string maps to (see build_graph's path_map).
    A real agent would inspect a structured tool_call/function_call field
    on the LLM's response instead of this simulated `answer == ""` check."""
    return "tools" if state["answer"] == "" else "end"


def build_graph():
    """Wires AgentState + the three functions above into a compiled,
    runnable LangGraph graph: agent -> (conditional) -> tools -> agent,
    looping until needs_tool routes to END."""
    graph = StateGraph(AgentState)
    graph.add_node("agent", fake_llm_decide)
    graph.add_node("tools", calculator_tool)

    graph.set_entry_point("agent")
    graph.add_conditional_edges("agent", needs_tool, {"tools": "tools", "end": END})
    graph.add_edge("tools", "agent")  # closes the loop: tool result feeds back into "agent"

    return graph.compile()


if __name__ == "__main__":
    app = build_graph()

    print("Compiled graph nodes:", list(app.get_graph().nodes))
    print()

    initial_state: AgentState = {
        "question": "What is 12 * 7?",
        "steps": [],
        "tool_result": None,
        "answer": "",
    }
    result = app.invoke(initial_state)

    print("Trace:")
    print("\n".join(result["steps"]))
    print("\nFinal answer:", result["answer"])
