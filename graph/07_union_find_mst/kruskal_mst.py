"""
Kruskal's Algorithm — Minimum Spanning Tree   (Difficulty: Hard)
Asked at: Google, Bloomberg — network design ("connect all cities cheapest")

Problem:
Given a weighted, undirected, connected graph, find a subset of edges
that connects all vertices with the minimum possible total edge weight,
and no cycles (a "spanning tree").

Example graph:
        (4)
    0 -------- 1
    | \        |
   (1) (2)   (2)
    |     \    |
    2 -----(5)-3

Flow (sort edges by weight, add if it doesn't form a cycle):
    Sorted edges: (0,2,1) (1,3,2) (0,3,2) (0,1,4) (2,3,5)
    Take (0,2,1)  -> ok, union(0,2)
    Take (1,3,2)  -> ok, union(1,3)
    Take (0,3,2)  -> ok, union(0,3) [connects the two components]
    Skip (0,1,4)  -> 0 and 1 already connected -> would form a cycle
    Skip (2,3,5)  -> already connected

    MST total weight: 1 + 2 + 2 = 5

Approach — Greedy + Union-Find:
1. Sort ALL edges by weight, ascending.
2. Walk through edges smallest first; add an edge to the MST only if its
   two endpoints are in different Union-Find sets (adding it wouldn't
   create a cycle).
3. Stop once you've added (V - 1) edges — that's a spanning tree.

Time Complexity:  O(E log E) — dominated by sorting the edges.
Space Complexity: O(V + E)
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        self.parent[root_x] = root_y
        return True


def kruskal_mst(n, edges):
    """edges = [(u, v, weight), ...]  ->  returns (mst_edges, total_weight)"""
    edges = sorted(edges, key=lambda edge: edge[2])
    uf = UnionFind(n)

    mst_edges = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == n - 1:
                break

    return mst_edges, total_weight


if __name__ == "__main__":
    n = 4
    edges = [(0, 1, 4), (0, 2, 1), (0, 3, 2), (1, 3, 2), (2, 3, 5)]

    mst_edges, total_weight = kruskal_mst(n, edges)
    print("MST edges:", mst_edges)
    print("Total weight:", total_weight)
