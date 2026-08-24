"""
Word Embeddings from Co-occurrence Counts - Distributional Semantics   (Topic: Embeddings)

Problem:
Demonstrate, with no external dependencies, the actual mechanism behind
the Data Flow Diagram in interview_qa.md: raw text -> "embedding model" ->
vectors positioned so that semantically related words land close together
and unrelated words land far apart. A real embedding model learns this
geometry with a neural network trained on billions of tokens; this toy
version learns it directly from co-occurrence counts over a tiny corpus,
so the mechanism is easy to trace by hand (see interview_qa.md Q M8 -
the distributional hypothesis).

Approach:
- Tokenize every sentence in the corpus (lowercase, strip punctuation,
  split on whitespace) and collect the vocabulary of every distinct word
  seen (tokenize).
- For each word, slide a window of `window` positions in both directions
  across every sentence it appears in, and count how often every other
  vocabulary word falls inside that window (build_cooccurrence_vectors).
  This produces one dense vector per word, with one dimension per
  vocabulary word - words that tend to appear near the same neighbors end
  up with similar vectors, purely from usage patterns, with no labels.
- Compare vectors with cosine_similarity (dot product over the product of
  magnitudes, computed from scratch with math.sqrt, with a zero-vector
  guard), and use l2_normalize to rescale a vector to unit length so that
  comparison becomes a plain dot product (see interview_qa.md Q M5 / P6).

Time Complexity:  O(total corpus tokens x window) to build all vectors;
                   O(vocab size) per cosine_similarity / l2_normalize call.
Space Complexity: O(vocab size^2) overall - one dense vector of length
                   |vocab| per word - which is exactly why this doesn't
                   scale to a real vocabulary (see interview_qa.md Q P4).
"""

import math


def tokenize(text: str) -> list:
    """Lowercase, strip punctuation, split on whitespace."""
    cleaned = "".join(ch if (ch.isalnum() or ch.isspace()) else " " for ch in text.lower())
    return cleaned.split()


def build_cooccurrence_vectors(sentences: list, window: int = 2) -> dict:
    """Build one dense co-occurrence vector per vocabulary word.

    For every word in every sentence, look `window` positions to the left
    and right (never crossing a sentence boundary) and increment a count
    for each neighbor seen. The resulting vector for a word has one entry
    per vocabulary word, in sorted vocab order.
    """
    tokenized = [tokenize(sentence) for sentence in sentences]
    vocab = sorted({word for sentence in tokenized for word in sentence})
    index = {word: i for i, word in enumerate(vocab)}

    vectors = {word: [0] * len(vocab) for word in vocab}
    for sentence in tokenized:
        for i, word in enumerate(sentence):
            left = max(0, i - window)
            right = min(len(sentence), i + window + 1)
            for j in range(left, right):
                if j == i:
                    continue
                neighbor = sentence[j]
                vectors[word][index[neighbor]] += 1
    return vectors


def cosine_similarity(v1: list, v2: list) -> float:
    """cos(theta) between two vectors: dot product over product of magnitudes."""
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        # a zero vector (e.g. a word with no recorded neighbors) has no
        # direction to compare -- define similarity as 0 rather than
        # dividing by zero
        return 0.0
    return dot / (norm1 * norm2)


def l2_normalize(vector: list) -> list:
    """Rescale a vector to unit length (L2 norm = 1), preserving direction."""
    norm = math.sqrt(sum(x * x for x in vector))
    if norm == 0:
        return list(vector)
    return [x / norm for x in vector]


if __name__ == "__main__":
    CORPUS = [
        "cat sat mat",
        "cat sat rug",
        "kitten sat mat",
        "kitten sat rug",
        "cat played kitten",
        "small kitten chased cat",
        "cat is small furry animal",
        "kitten is small furry animal",
        "stocks fell sharply today",
        "shares fell sharply today",
        "investors watched stocks closely",
        "investors watched shares closely",
        "traders sold stocks in market",
        "traders sold shares in market",
        "stocks are risky investment",
        "shares are risky investment",
    ]

    print("tokenize() lowercases and strips punctuation:")
    print(" ", tokenize("The Cat, sat on the MAT!"))

    vectors = build_cooccurrence_vectors(CORPUS, window=2)
    print(f"\nBuilt co-occurrence vectors for {len(vectors)} words "
          f"(each vector has {len(vectors['cat'])} dimensions = vocab size).\n")

    def show(word1, word2):
        sim = cosine_similarity(vectors[word1], vectors[word2])
        print(f"  cosine_similarity({word1!r:>10}, {word2!r:>10}) = {round(sim, 3)}")

    print("Related pairs (same semantic cluster) -- expect HIGH similarity:")
    show("cat", "kitten")
    show("mat", "rug")
    show("stocks", "shares")

    print("\nUnrelated pairs (different semantic cluster) -- expect LOW similarity:")
    show("cat", "stocks")
    show("kitten", "shares")
    show("mat", "market")

    print("\nL2-normalizing first turns cosine similarity into a plain dot product:")
    n1 = l2_normalize(vectors["cat"])
    n2 = l2_normalize(vectors["kitten"])
    dot_product = sum(a * b for a, b in zip(n1, n2))
    print(f"  dot(l2_normalize(cat), l2_normalize(kitten)) = {round(dot_product, 3)}")
    print(f"  cosine_similarity(cat, kitten)                = "
          f"{round(cosine_similarity(vectors['cat'], vectors['kitten']), 3)}")
