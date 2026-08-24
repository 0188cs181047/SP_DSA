"""
Retrieval-Augmented Generation - Toy Bag-of-Words RAG Pipeline   (Topic: RAG)

Problem:
Demonstrate, with no external dependencies, the actual mechanism behind the
data flow diagram in interview_qa.md: documents -> chunk -> embed -> index,
then query -> embed -> retrieve top-K -> build an augmented prompt -> LLM ->
grounded answer. A real system embeds text with a neural network (e.g. a
sentence-transformer) and searches with an ANN index; this toy version
embeds with plain bag-of-words term frequency and searches with a
brute-force cosine-similarity scan, so every step is easy to trace and
print by hand.

Approach:
- Split each document into sentence-level chunks (chunk_documents), tagging
  every chunk with its source doc id and a global chunk id.
- Build a fixed vocabulary from the corpus and embed every chunk as a
  bag-of-words term-frequency vector over that vocabulary (embed) -- this
  is clearly NOT a real embedding (no semantics, no synonyms, just literal
  word-overlap counts), which is exactly what makes it easy to trace
  retrieval by hand.
- At query time, embed the query the same way, score it against every
  indexed chunk with cosine_similarity, and keep the top-K highest scoring
  chunks (retrieve) -- a brute-force O(n) scan standing in for a real ANN
  index (see the vector-databases topic for that).
- Assemble the retrieved chunks and the original question into one prompt
  string (build_augmented_prompt), and hand it to a stand-in fake_llm() in
  place of a real hosted LLM call.

Time Complexity:  O(len(corpus)) to tokenize/chunk/index; O(n x |vocab|) per
                   retrieve() call, scanning all n indexed chunks.
Space Complexity: O(n x |vocab|) to store one dense term-frequency vector
                   per chunk -- the toy analogue of why real vector
                   databases use compact learned embeddings plus ANN
                   indexes instead of raw per-document term vectors once
                   corpus size grows.
"""

import math
import re
from collections import Counter


def tokenize(text):
    # lowercase word extraction -- no stemming, no stopword removal, just
    # the bare minimum needed to turn text into comparable tokens
    return re.findall(r"[a-z0-9]+", text.lower())


def embed(text, vocab):
    # STAND-IN for a real embedding model: a bag-of-words term-frequency
    # vector over a FIXED vocabulary. No semantics -- "finished" and
    # "completed" share zero dimensions here, unlike a real embedding
    # (see interview_qa.md Practical P2).
    tokens = tokenize(text)
    counts = Counter(tokens)
    total = len(tokens) or 1  # avoid ZeroDivisionError on empty text
    return [counts.get(term, 0) / total for term in vocab]


def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0  # no overlap / empty vector -> similarity defined as 0, not an error
    return dot / (norm1 * norm2)


def chunk_documents(documents, chunk_size=1):
    # Sentence-level chunking: split on sentence-ending punctuation, then
    # group `chunk_size` sentences per chunk. chunk_size=1 is most granular;
    # chunk_size >= a document's sentence count collapses back to one chunk
    # per document (see interview_qa.md Practical P1).
    chunks = []
    for doc_id, doc_text in enumerate(documents):
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", doc_text.strip()) if s.strip()]
        for i in range(0, len(sentences), chunk_size):
            group = sentences[i:i + chunk_size]
            chunks.append({
                "doc_id": doc_id,
                "chunk_id": len(chunks),
                "text": " ".join(group),
            })
    return chunks


def build_index(chunks, vocab):
    # Offline step: one (chunk, vector) pair per chunk, computed once and reused for every query.
    return [(chunk, embed(chunk["text"], vocab)) for chunk in chunks]


def retrieve(query, index, vocab, k=2):
    # Brute-force O(n) scan -- fine for a demo corpus, see interview_qa.md
    # Practical P3 for when this needs to become an ANN index instead.
    query_vec = embed(query, vocab)
    scored = [(cosine_similarity(query_vec, vec), chunk) for chunk, vec in index]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:k]


def build_augmented_prompt(query, retrieved_chunks):
    context_block = "\n".join(
        f"[{i + 1}] (doc {chunk['doc_id']}, chunk {chunk['chunk_id']}): {chunk['text']}"
        for i, (_score, chunk) in enumerate(retrieved_chunks)
    )
    return (
        "Answer the question using ONLY the context below. "
        "Cite sources like [1], [2] where relevant.\n\n"
        f"Context:\n{context_block}\n\n"
        f"Question: {query}\n"
        "Answer:"
    )


def fake_llm(prompt):
    # STUB standing in for a real LLM API call, e.g.
    # client.messages.create(model=..., messages=[{"role": "user", "content": prompt}]).
    # No network, no API key, no randomness -- just enough to prove the
    # retrieved context actually reached the prompt, by echoing back
    # whatever text is tagged [1] (the top-ranked retrieved chunk).
    top_chunk_line = next((line for line in prompt.splitlines() if line.startswith("[1]")), "")
    fact = top_chunk_line.split(":", 1)[1].strip() if ":" in top_chunk_line else "(no context retrieved)"
    return f"(fake_llm stub) Grounded answer using [1]: {fact}"


if __name__ == "__main__":
    documents = [
        "The Eiffel Tower is located in Paris, France. It was completed in 1889 for the World's Fair. "
        "The tower is made of wrought iron and stands about 330 meters tall.",

        "The Great Wall of China stretches over 21000 kilometers. It was built over many centuries to "
        "protect against invasions from northern nomadic groups. Construction began more than 2000 years ago.",

        "The Statue of Liberty stands in New York Harbor. It was a gift from France to the United States, "
        "dedicated in 1886. The statue represents freedom and democracy.",

        "Machu Picchu is an ancient Incan city located high in the Andes mountains of Peru. "
        "It sits at about 2430 meters of elevation. The site was rediscovered by the outside world in 1911.",
    ]

    chunks = chunk_documents(documents, chunk_size=1)
    vocab = sorted(set(tokenize(" ".join(chunk["text"] for chunk in chunks))))
    index = build_index(chunks, vocab)

    print(f"Indexed {len(chunks)} chunks from {len(documents)} documents, vocab size {len(vocab)}.\n")

    query = "Where is the Eiffel Tower located?"
    top_k = retrieve(query, index, vocab, k=2)

    print(f"Query: {query!r}\n")
    print("Retrieved chunks:")
    for score, chunk in top_k:
        print(f"  score={score:.3f}  (doc {chunk['doc_id']}, chunk {chunk['chunk_id']}): {chunk['text']!r}")

    prompt = build_augmented_prompt(query, top_k)
    print("\nAugmented prompt sent to the LLM:")
    print("-" * 60)
    print(prompt)
    print("-" * 60)

    answer = fake_llm(prompt)
    print("\nfake_llm output:")
    print(answer)

    print("\n" + "=" * 60)
    print("Same query, but chunk_size=10 (collapses to ~one chunk per document):")
    coarse_chunks = chunk_documents(documents, chunk_size=10)
    coarse_vocab = sorted(set(tokenize(" ".join(c["text"] for c in coarse_chunks))))
    coarse_index = build_index(coarse_chunks, coarse_vocab)
    coarse_top_k = retrieve(query, coarse_index, coarse_vocab, k=1)
    for score, chunk in coarse_top_k:
        print(f"  score={score:.3f}  (doc {chunk['doc_id']}): {chunk['text'][:100]}...")
    print("The one relevant sentence is now diluted inside a whole document's")
    print("worth of text instead of being its own tight, focused chunk -- the")
    print("failure mode discussed in Practical P1 and the Lost-in-the-Middle")
    print("question (Medium M5).")
