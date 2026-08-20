"""
Union-Find (Disjoint Set Union)   (Difficulty: Medium)
Asked at: Google, Meta, Amazon — the go-to structure for "are these connected?"

Problem:
Maintain a collection of disjoint sets that supports two operations
efficiently:
  - union(x, y): merge the sets containing x and y
  - find(x):     which set does x belong to? (returns a representative)

Used to detect cycles, count connected components, and build MSTs
(Kruskal's algorithm).

Example:
    union(0, 1), union(1, 2), union(3, 4)

Flow diagram (path compression flattens the tree over time):
    Before compression:      After find(2) with compression:
        0                          0
        |                        / | \
        1                       1  2  (both now point straight to root)
        |
        2

    find(0) == find(2)  -> True  (0 and 2 are in the same set)
    find(0) == find(3)  -> False (different sets)

Approach — two optimizations make this nearly O(1) per operation:
1. Path Compression (in find): while walking up to the root, make every
   node point directly to the root, so future lookups are instant.
2. Union by Rank/Size (in union): always attach the smaller tree under
   the bigger tree's root, keeping trees shallow.

Time Complexity:  ~O(α(n)) per operation (α = inverse Ackermann, effectively
                  constant for any realistic input size).
Space Complexity: O(n)
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return False  # already connected -> this edge would form a cycle

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    print("0 and 2 connected?", uf.connected(0, 2))
    print("0 and 3 connected?", uf.connected(0, 3))
    print("Union(0,1) again forms a cycle?", not uf.union(0, 1))
