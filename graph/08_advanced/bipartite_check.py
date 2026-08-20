"""
Is Graph Bipartite?   (Difficulty: Medium)
Asked at: Meta, Google, Amazon

Problem:
A graph is bipartite if its nodes can be split into two groups such that
every edge connects a node from group A to a node from group B (no edge
stays within the same group). Equivalent to: can the graph be colored
with 2 colors such that no two adjacent nodes share a color?

Example (bipartite):
    0 --- 1        Color 0: {0, 2}
    |     |        Color 1: {1, 3}
    3 --- 2        Every edge crosses colors -> bipartite

Example (NOT bipartite — odd cycle):
    0 --- 1
     \\   /
      \\ /
       2            0-1-2-0 is a 3-cycle (odd length) -> impossible
                    to 2-color without a clash

Flow (BFS coloring):
    color[0] = 0
    color[1] = 1 (neighbor of 0, must differ)
    color[2] = 0 (neighbor of 1, must differ)
    check edge 2-0: both color 0 -> CLASH -> not bipartite

Approach:
- BFS/DFS from every unvisited node, coloring it, then alternating the
  color for every neighbor.
- If you ever find a neighbor that already has the SAME color as the
  current node, the graph is not bipartite.
- Key insight: a graph is bipartite if and only if it contains no odd-
  length cycle.

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import deque, defaultdict


def is_bipartite(graph, n):
    color = {}

    for start in range(n):
        if start in color:
            continue

        color[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

    return True


if __name__ == "__main__":
    bipartite_graph = defaultdict(list, {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2],
    })

    odd_cycle_graph = defaultdict(list, {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
    })

    print("Square graph is bipartite?", is_bipartite(bipartite_graph, 4))
    print("Triangle graph is bipartite?", is_bipartite(odd_cycle_graph, 3))
