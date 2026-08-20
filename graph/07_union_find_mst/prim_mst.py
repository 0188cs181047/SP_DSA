"""
Prim's Algorithm — Minimum Spanning Tree   (Difficulty: Hard)
Asked at: Google, Bloomberg — same problem as Kruskal, different strategy

Problem:
Same as Kruskal's: find the minimum-weight set of edges that connects
all vertices with no cycles. Prim's grows the tree one vertex at a time
instead of sorting all edges up front — better when the graph is dense.

Example graph:
        (4)
    0 -------- 1
    | \        |
   (1) (2)   (2)
    |     \    |
    2 -----(5)-3

Flow (grow the tree from node 0, always add the cheapest edge leaving it):
    tree = {0}
    cheapest edge leaving tree: (0,2,1)  -> add 2.   tree = {0,2}
    cheapest edge leaving tree: (0,3,2) or (2,3,5)  -> pick (0,3,2). tree={0,2,3}
    cheapest edge leaving tree: (1,3,2)  -> add 1.   tree = {0,1,2,3}

    MST total weight: 1 + 2 + 2 = 5   (same answer as Kruskal — MST weight
    is unique even if the chosen edges differ)

Approach — Greedy + Min-Heap (very similar shape to Dijkstra):
1. Start from any node, push its edges into a min-heap keyed by weight.
2. Pop the cheapest edge; if it leads to a node NOT yet in the tree, add
   that node to the tree and push all of its outgoing edges too.
3. Skip edges that lead to a node already in the tree (would be a cycle).
4. Repeat until all V nodes are in the tree.

Time Complexity:  O(E log E) with a binary heap.
Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict


def prim_mst(n, edges):
    """edges = [(u, v, weight), ...]  ->  returns (mst_edges, total_weight)"""
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    visited = {0}
    min_heap = list(graph[0])
    heapq.heapify(min_heap)

    mst_edges = []
    total_weight = 0

    while min_heap and len(visited) < n:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        mst_edges.append((weight, node))
        total_weight += weight

        for next_weight, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (next_weight, neighbor))

    return mst_edges, total_weight


if __name__ == "__main__":
    n = 4
    edges = [(0, 1, 4), (0, 2, 1), (0, 3, 2), (1, 3, 2), (2, 3, 5)]

    mst_edges, total_weight = prim_mst(n, edges)
    print("MST edges (weight, node):", mst_edges)
    print("Total weight:", total_weight)
