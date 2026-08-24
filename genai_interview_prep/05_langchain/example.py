"""
LCEL Chain Composition -- Real langchain-core with a Fake Model   (Topic: LangChain)

Problem:
Demonstrate the actual mechanism behind the "prompt | model | parser" pipe
from interview_qa.md using the REAL langchain-core library, not a
from-scratch reimplementation -- unlike most other topics in this repo,
LangChain IS the library being interviewed about, so using it directly is
the entire point. To still run with no API key and no network access, the
model slot is filled by FakeListChatModel, a real, built-in LangChain
testing utility that cycles through a list of canned string responses
instead of calling a provider. Swapping it for a real provider (e.g.
ChatAnthropic(model="claude-...")) requires changing exactly one line --
see Q P1 in interview_qa.md.

Approach:
- build_chain wires a ChatPromptTemplate, a FakeListChatModel, and a
  StrOutputParser into one Runnable with the `|` operator (LCEL). Every
  piece implements the same invoke/batch/stream/ainvoke interface, so `|`
  is the only composition primitive needed regardless of what sits on
  either side of it.
- build_rag_chain shows the retrieval-augmented variant from the Data Flow
  Diagram in interview_qa.md: RunnableParallel fans the same raw question
  out to two branches at once -- fake_retriever (a tiny keyword-matching
  stand-in for a vector store, searching the _DOCS dict) and
  RunnablePassthrough (which forwards the question unchanged) -- then
  merges both branches into the {context, question} dict the prompt
  template needs, before continuing on to model | parser exactly like
  build_chain does.
- __main__ drives both chains, calling .invoke() twice and .stream() once
  on the plain chain, then .invoke() twice on the RAG chain. Each
  FakeListChatModel instance is given exactly as many canned responses as
  calls it will serve, so nothing here relies on FakeListChatModel's
  cycle-back-to-the-start wraparound behavior.

Time Complexity:  Each FakeListChatModel call is O(1) list indexing (a real
                   provider replaces this with a network round trip, which
                   dominates end-to-end latency in production instead).
                   .stream() is O(len(response)) since FakeListChatModel
                   simulates token-level streaming by yielding one
                   character-chunk at a time (see Q P2). fake_retriever is
                   O(len(_DOCS)) keyword scans, standing in for a real
                   vector similarity search.
Space Complexity: O(number of canned responses) held by each
                   FakeListChatModel instance, plus O(prompt size) per
                   call -- no conversation memory is retained across calls
                   in either chain here.
"""

try:
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.language_models.fake_chat_models import FakeListChatModel
    from langchain_core.runnables import Runnable, RunnableParallel, RunnablePassthrough
except ImportError:
    print(
        "This example needs the real langchain-core library.\n"
        "Install it with:  pip install langchain-core"
    )
    raise SystemExit(1)


def build_chain(responses: list[str]) -> Runnable:
    """Build a prompt | model | parser LCEL chain. `responses` are canned
    replies for FakeListChatModel, standing in for a real provider so this
    file runs with no API key -- swap in e.g. ChatAnthropic(model=...) for
    real use, with zero other changes to this function."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a concise, factual assistant."),
        ("human", "{question}"),
    ])
    model = FakeListChatModel(responses=responses)
    parser = StrOutputParser()
    return prompt | model | parser


# Tiny in-memory "corpus", standing in for a real vector store / document
# index. fake_retriever below does keyword matching instead of embedding
# similarity search, but it satisfies the same contract a real retriever
# would: given a query string, return relevant context as a string.
_DOCS = {
    "lcel": "LCEL is LangChain's pipe-based syntax for composing Runnables.",
    "runnable": "A Runnable is the common invoke/batch/stream/ainvoke interface every LangChain component implements.",
    "memory": "Memory persists conversation state across turns because a raw LLM call is stateless.",
}


def fake_retriever(question: str) -> str:
    """Return the first canned doc whose keyword appears in `question`,
    standing in for a real vector-store similarity search."""
    lowered = question.lower()
    for keyword, doc in _DOCS.items():
        if keyword in lowered:
            return doc
    return "No relevant document found."


def build_rag_chain(responses: list[str]) -> Runnable:
    """Extend build_chain into the RAG variant from the Data Flow Diagram.
    RunnableParallel fans the single raw-question input out to two branches
    at once -- fake_retriever and RunnablePassthrough -- and merges their
    outputs into the {context, question} dict the prompt template expects,
    before continuing on to model | parser exactly like build_chain."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer using ONLY the provided context. If the context doesn't cover it, say so."),
        ("human", "Context: {context}\n\nQuestion: {question}"),
    ])
    model = FakeListChatModel(responses=responses)
    parser = StrOutputParser()

    retrieve = RunnableParallel(
        context=fake_retriever,          # plain function, auto-coerced to a RunnableLambda
        question=RunnablePassthrough(),  # forwards the raw input string unchanged
    )
    return retrieve | prompt | model | parser


if __name__ == "__main__":
    print("=== Plain chain: prompt | model | parser ===\n")
    chain = build_chain(responses=[
        "LCEL stands for LangChain Expression Language.",
        "A Runnable is the common invoke/batch/stream/ainvoke interface.",
        "Streaming yields output incrementally instead of all at once.",
    ])

    for question in ("What is LCEL?", "What is a Runnable?"):
        answer = chain.invoke({"question": question})
        print(f"Q: {question}\nA: {answer}\n")

    print("Streaming a third question, one chunk at a time:")
    chunks = []
    for chunk in chain.stream({"question": "What does streaming do?"}):
        chunks.append(chunk)
        print(f"  chunk: {chunk!r}")
    print(f"Reassembled: {''.join(chunks)!r}")
    print(f"({len(chunks)} chunks -- FakeListChatModel simulates real "
          f"token-level streaming by yielding one character at a time)\n")

    print("=== RAG chain: RunnableParallel(retriever, passthrough) | prompt | model | parser ===\n")
    rag_chain = build_rag_chain(responses=[
        "Based on the context, LCEL is LangChain's pipe-based composition syntax.",
        "Based on the context, memory exists because LLM calls are stateless.",
    ])

    for question in ("What is LCEL?", "Why do we need memory?"):
        answer = rag_chain.invoke(question)
        print(f"Q: {question}\nA: {answer}\n")
