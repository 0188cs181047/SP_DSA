"""
Mini Tracer + Dataset Evaluator - Decorator-Based Observability   (Topic: LangSmith)

Problem:
Demonstrate, with no external dependencies and no API key, the actual mechanism
behind the Data Flow Diagram in interview_qa.md: every step of a pipeline gets
wrapped in a span (name, inputs, output, duration) that lands in a trace log,
and a dataset of examples can be run through that pipeline and scored by an
evaluator to produce a repeatable quality benchmark. Real LangSmith does this
with a hosted trace store, a web dashboard, and (optionally) an LLM-as-judge
evaluator; this toy version does it with a plain module-level list and a
substring-match evaluator, so the whole mechanism fits on one screen.

Approach:
- `traceable(name)` is a decorator factory (mirrors langsmith.traceable): it
  wraps a function so every call is timed and appended to TRACE_LOG as one
  span - name, inputs, output, duration_ms. See interview_qa.md Q P1 for why
  this only produces a FLAT list, not a nested trace tree like real LangSmith.
- `retrieve` and `generate` are each traced separately, and `rag_pipeline`
  calls both, so one pipeline invocation produces three spans in TRACE_LOG -
  the toy version of "one trace, multiple nested runs."
- `exact_match_evaluator` scores a pipeline output against an expected
  substring (1.0 / 0.0) - a stand-in for LangSmith's built-in and
  LLM-as-judge evaluators (see interview_qa.md Q P2 for where this breaks).
- `run_evaluation` runs a small dataset of {query, expected} examples through
  a pipeline, scores each with an evaluator, warns on any example below a
  threshold, and returns the average score - a from-scratch version of a
  LangSmith evaluation experiment (see interview_qa.md Q P5).

Time Complexity:  O(len(dataset)) pipeline calls in run_evaluation; each call
                   is O(1) (fixed-size in-memory knowledge base lookup).
                   Tracing overhead per call is O(1) (one dict append).
Space Complexity: O(number of traced calls made so far) for TRACE_LOG, since
                   it is a module-level list that only ever grows.
"""

import time
import functools

# ---------------------------------------------------------------------------
# Reference only -- NOT executed. This is what the same instrumentation looks
# like with the real LangSmith SDK instead of the from-scratch stand-in below:
#
#   from langsmith import traceable
#
#   # required for traces to actually reach the LangSmith dashboard:
#   #   export LANGCHAIN_TRACING_V2=true
#   #   export LANGCHAIN_API_KEY=ls__...
#   #   export LANGCHAIN_PROJECT=my-rag-app        # optional, defaults to "default"
#
#   @traceable(name="retrieve")
#   def retrieve(query: str) -> list[str]:
#       ...
#
# Everything below re-implements just enough of that idea to run anywhere,
# with zero network calls and zero third-party dependencies.
# ---------------------------------------------------------------------------

TRACE_LOG = []


def traceable(name):
    """Tiny stand-in for langsmith.traceable: records one span per call into
    TRACE_LOG (name, inputs, output, duration_ms). See interview_qa.md Q P1
    for the flat-list-vs-nested-tree discussion this deliberately sets up."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            output = fn(*args, **kwargs)
            duration_ms = (time.perf_counter() - start) * 1000
            TRACE_LOG.append({
                "name": name,
                "inputs": {"args": args, "kwargs": kwargs},
                "output": output,
                "duration_ms": round(duration_ms, 3),
            })
            return output
        return wrapper
    return decorator


# a tiny in-memory "knowledge base" standing in for a real vector store
_KNOWLEDGE_BASE = {
    "eiffel tower": "The Eiffel Tower is a wrought-iron tower in Paris, France, completed in 1889.",
    "great wall": "The Great Wall of China is a series of fortifications across northern China.",
    "colosseum": "The Colosseum is an ancient amphitheater in Rome, Italy, completed in 80 AD.",
}


@traceable("retrieve")
def retrieve(query):
    """Fake retrieval step: naive keyword lookup standing in for a real
    embedding + vector-store search."""
    time.sleep(0.01)  # stand-in for real retrieval network latency
    query_lower = query.lower()
    matches = [doc for key, doc in _KNOWLEDGE_BASE.items() if key in query_lower]
    return matches if matches else ["No matching document found."]


@traceable("generate")
def generate(query, docs):
    """Fake generation step: a templated answer built from retrieved docs,
    standing in for an actual LLM call."""
    time.sleep(0.01)  # stand-in for real model call latency
    if docs == ["No matching document found."]:
        return f"I don't have information about {query}."
    return f"{query} -- {docs[0]}"


@traceable("rag_pipeline")
def rag_pipeline(query):
    """One end-to-end RAG call: retrieve context, then generate an answer
    from it. Produces three spans in TRACE_LOG per call (see Q P1)."""
    docs = retrieve(query)
    return generate(query, docs)


def exact_match_evaluator(output, expected):
    """1.0 if `expected` appears as a substring of `output` (case-insensitive),
    else 0.0 -- see interview_qa.md Q P2 for why this is a blunt instrument."""
    return 1.0 if expected.lower() in output.lower() else 0.0


def run_evaluation(dataset, pipeline, evaluator=exact_match_evaluator, warn_below=0.5):
    """Run `pipeline` over every example in `dataset`, score each output with
    `evaluator`, print a per-example result (flagging anything below
    `warn_below`), and return the average score -- a from-scratch version of
    a LangSmith evaluation experiment (see interview_qa.md Q P5)."""
    scores = []
    for example in dataset:
        query, expected = example["query"], example["expected"]
        output = pipeline(query)
        score = evaluator(output, expected)
        scores.append(score)

        status = "OK" if score >= warn_below else "WARNING: below threshold"
        print(f"[{status}] query={query!r} score={score} output={output!r}")

    average = sum(scores) / len(scores) if scores else 0.0
    print(f"\nAverage score over {len(scores)} examples: {average:.2f}")
    return average


if __name__ == "__main__":
    print("=== Running rag_pipeline once ===")
    print("Answer:", rag_pipeline("Eiffel Tower"))

    print("\n=== TRACE_LOG after one pipeline call ===")
    for span in TRACE_LOG:
        print(span)

    print("\n=== Running evaluation over a small dataset ===")
    dataset = [
        {"query": "Eiffel Tower", "expected": "Paris"},
        {"query": "Great Wall", "expected": "China"},
        {"query": "Statue of Liberty", "expected": "New York"},  # not in the KB -> should warn
    ]
    run_evaluation(dataset, rag_pipeline)
