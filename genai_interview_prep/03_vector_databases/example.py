"""
Vector Similarity Search - Brute-Force Flat Index vs. Random-Projection LSH   (Topic: Vector Databases)

Problem:
Demonstrate, with no external dependencies, the actual mechanism behind the
Data Flow Diagram in interview_qa.md: embed -> index -> ANN search -> top-K
+ metadata. A real vector database builds HNSW/IVF-style structures on top
of a compiled ANN library (FAISS, HNSWlib); this toy version builds the two
ends of that spectrum from scratch so the approximate-vs-exact trade-off is
directly visible: FlatVectorStore is the brute-force baseline every ANN
index is measured against, and RandomProjectionLSH is a minimal, real (but
simplified) ANN index that can be shown missing a true nearest neighbor
that brute force always finds.

Approach:
- cosine_similarity computes similarity from scratch (dot product over the
  product of magnitudes) -- no numpy needed for these small demo vectors.
- FlatVectorStore.search compares the query against every stored vector
  (O(n) per query) and optionally applies a `where` metadata predicate
  before ranking -- the same approach a naive "just loop over rows"
  implementation would take.
- RandomProjectionLSH hashes each vector by the sign of its dot product
  with a fixed set of random hyperplanes (_hash), bucketing vectors that
  fall on the same side of every plane together. search() only scores
  candidates sharing the query's exact bucket key, so a true nearest
  neighbor sitting just across one plane boundary is never even
  considered -- this is precisely what makes an ANN index "approximate."
- The __main__ block first runs a small, hand-crafted 3D example (two
  obvious topic clusters) so the ranking is easy to sanity-check by eye,
  then generates a larger set of random vectors and searches over several
  query points until RandomProjectionLSH's top-1 result disagrees with
  FlatVectorStore's, to make the recall trade-off concrete rather than
  theoretical.

Time Complexity:  FlatVectorStore.search is O(n * d) per query (n stored
                   vectors, d dimensions). RandomProjectionLSH.search is
                   O(b * d + p * d), where b is the number of vectors
                   sharing the query's bucket and p is num_planes --
                   typically b << n, which is the entire point of bucketing.
Space Complexity: O(n * d) for both -- every vector is stored in full; the
                   LSH index additionally stores num_planes vectors of
                   length d for the random hyperplanes themselves.
"""

import math
import random
from collections import defaultdict


def cosine_similarity(v1, v2):
    """Cosine similarity from scratch: dot(v1, v2) / (||v1|| * ||v2||)."""
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


class FlatVectorStore:
    """Brute-force baseline: O(n) comparisons per query, always exact."""

    def __init__(self):
        self._vectors = {}
        self._metadata = {}

    def add(self, doc_id, vector, metadata=None):
        self._vectors[doc_id] = vector
        self._metadata[doc_id] = metadata or {}

    def search(self, query_vector, k=3, where=None):
        """Return the top-k (doc_id, score) pairs by cosine similarity.

        `where`, if given, is a callable(metadata) -> bool; documents whose
        metadata fails the predicate are excluded before ranking (a
        "pre-filter", see interview_qa.md Q P4).
        """
        scored = []
        for doc_id, vector in self._vectors.items():
            if where is not None and not where(self._metadata[doc_id]):
                continue
            scored.append((cosine_similarity(query_vector, vector), doc_id))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [(doc_id, round(score, 4)) for score, doc_id in scored[:k]]


class RandomProjectionLSH:
    """Minimal locality-sensitive hashing index -- a simplified stand-in
    for HNSW/IVF-style ANN.

    Buckets vectors by which side of `num_planes` random hyperplanes they
    fall on. search() only scores vectors sharing the query's exact bucket
    key, so it can miss a neighbor sitting just across a plane boundary --
    that restriction is what makes it approximate instead of exact.
    """

    def __init__(self, dim, num_planes=4, seed=42):
        rng = random.Random(seed)
        self.dim = dim
        self.num_planes = num_planes
        self.planes = [[rng.gauss(0, 1) for _ in range(dim)] for _ in range(num_planes)]
        self.buckets = defaultdict(list)
        self._vectors = {}

    def _hash(self, vector):
        # Sign of the dot product with each random hyperplane -> one bit per
        # plane. Points on the same side of every plane share a bucket key
        # (see interview_qa.md Q P2 for why that makes it "locality-sensitive").
        bits = (
            "1" if sum(v * p for v, p in zip(vector, plane)) >= 0 else "0"
            for plane in self.planes
        )
        return "".join(bits)

    def add(self, doc_id, vector):
        self._vectors[doc_id] = vector
        self.buckets[self._hash(vector)].append(doc_id)

    def search(self, query_vector, k=3):
        key = self._hash(query_vector)
        scored = [
            (cosine_similarity(query_vector, self._vectors[doc_id]), doc_id)
            for doc_id in self.buckets.get(key, [])
        ]
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [(doc_id, round(score, 4)) for score, doc_id in scored[:k]]


if __name__ == "__main__":
    # ---- Part 1: small, hand-crafted 3D dataset -----------------------------
    # Two obvious "topic clusters" so the ranking is easy to sanity-check by eye.
    documents = [
        ("doc_cat_1", [1.0, 0.9, 0.0], {"topic": "animals"}),
        ("doc_cat_2", [0.9, 1.0, 0.1], {"topic": "animals"}),
        ("doc_cat_3", [0.95, 0.85, 0.05], {"topic": "animals"}),
        ("doc_fin_1", [0.0, 0.1, 1.0], {"topic": "finance"}),
        ("doc_fin_2", [0.1, 0.0, 0.9], {"topic": "finance"}),
        ("doc_fin_3", [0.05, 0.05, 0.95], {"topic": "finance"}),
    ]

    flat_store = FlatVectorStore()
    small_lsh = RandomProjectionLSH(dim=3, num_planes=2, seed=7)
    for doc_id, vector, metadata in documents:
        flat_store.add(doc_id, vector, metadata)
        small_lsh.add(doc_id, vector)

    query = [1.0, 1.0, 0.0]  # clearly closer to the "animals" cluster
    print("=" * 72)
    print(f"PART 1: small hand-crafted dataset, query = {query}")
    print("=" * 72)
    print("FlatVectorStore     (exact, brute force) top-3:", flat_store.search(query, k=3))
    print("RandomProjectionLSH (approximate)        top-3:", small_lsh.search(query, k=3))

    print("\nMetadata filter demo -- same query, but restricted to topic == 'finance':")
    finance_only = flat_store.search(query, k=3, where=lambda md: md["topic"] == "finance")
    print("FlatVectorStore.search(query, where=topic=='finance'):", finance_only)

    # ---- Part 2: larger random dataset -- find a case where LSH misses ------
    # Bucket-restrict search means a true nearest neighbor can hide just
    # across a random hyperplane boundary. Sweep a few query points against
    # one fixed index until brute force and LSH disagree on the top-1 result.
    print("\n" + "=" * 72)
    print("PART 2: demonstrating LSH approximation error")
    print("=" * 72)
    rng = random.Random(123)
    dim = 8
    random_docs = [(f"rand_{i}", [rng.gauss(0, 1) for _ in range(dim)]) for i in range(30)]

    big_flat = FlatVectorStore()
    big_lsh = RandomProjectionLSH(dim=dim, num_planes=5, seed=99)
    for doc_id, vector in random_docs:
        big_flat.add(doc_id, vector)
        big_lsh.add(doc_id, vector)

    mismatch = None
    for attempt in range(1, 201):
        candidate_query = [rng.gauss(0, 1) for _ in range(dim)]
        exact_top1 = big_flat.search(candidate_query, k=1)[0]
        approx = big_lsh.search(candidate_query, k=1)
        if not approx or approx[0][0] != exact_top1[0]:
            mismatch = (attempt, candidate_query, exact_top1, approx)
            break

    if mismatch:
        attempt, q, exact_top1, approx = mismatch
        print(
            f"Found a mismatch after {attempt} query attempt(s) against "
            f"{len(random_docs)} random {dim}-dim vectors ({big_lsh.num_planes} planes):"
        )
        print("  FlatVectorStore     (exact)  nearest neighbor:", exact_top1)
        if approx:
            print("  RandomProjectionLSH (approx) top-1:          ", approx[0],
                  " <- different doc than the true nearest neighbor")
        else:
            print("  RandomProjectionLSH (approx) top-1:           None"
                  " -- the query's bucket had no candidates at all!")
        print(
            "\nThis is the ANN trade-off in one example: brute force always finds the "
            "true nearest neighbor; the LSH index only ever looks inside one bucket, "
            "so a neighbor sitting just across a random hyperplane boundary is invisible to it."
        )
    else:
        print(
            f"No mismatch found in 200 query attempts with {big_lsh.num_planes} planes -- "
            "try more planes (smaller buckets) or fewer, higher-dimensional points."
        )
