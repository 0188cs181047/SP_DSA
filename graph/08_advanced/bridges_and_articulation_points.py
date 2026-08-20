"""
Bridges and Articulation Points (Tarjan's Algorithm)   (Difficulty: Hard)
Asked at: Google, Bloomberg — network reliability / "single point of failure" analysis

Problem:
- Bridge: an edge whose removal DISCONNECTS the graph (increases the
  number of connected components).
- Articulation Point (Cut Vertex): a NODE whose removal disconnects the
  graph.
Both identify the fragile parts of a network — critical connections that
should not fail.

Example:
    0 --- 1 --- 3
    |     |
    2 ----+     4 --- 5

Flow diagram:
    - Edge (1, 3) is a BRIDGE: removing it isolates node 3.
    - Node 1 is an ARTICULATION POINT: removing it disconnects {0,2} from {3}.
    - Edge (0,1)/(1,2)/(0,2) are NOT bridges — they're part of a cycle
      (0-1-2-0), so there's an alternate path even if one is removed.

Approach — DFS with discovery time & low-link value:
- disc[u]: the order/time u was first visited in DFS.
- low[u]:  the earliest discovery time reachable from u's subtree using
           AT MOST ONE back-edge (an edge to an ancestor).
- Bridge rule: edge (u, v) [v is a DFS child of u] is a bridge if
  low[v] > disc[u]  — meaning v's subtree has NO way back to u or any
  ancestor of u except through this exact edge.
- Articulation point rule: u is a cut vertex if either
    (a) u is the DFS root with 2+ children, or
    (b) u is not the root and some child v has low[v] >= disc[u].

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict


class BridgeFinder:
    def __init__(self, n, edges):
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.n = n
        self.disc = [-1] * n
        self.low = [-1] * n
        self.timer = 0
        self.bridges = []
        self.articulation_points = set()

    def run(self):
        for node in range(self.n):
            if self.disc[node] == -1:
                self._dfs(node, parent=-1)
        return self.bridges, self.articulation_points

    def _dfs(self, u, parent):
        self.disc[u] = self.low[u] = self.timer
        self.timer += 1
        children = 0

        for v in self.graph[u]:
            if v == parent:
                continue

            if self.disc[v] == -1:
                children += 1
                self._dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] > self.disc[u]:
                    self.bridges.append((u, v))

                if parent != -1 and self.low[v] >= self.disc[u]:
                    self.articulation_points.add(u)
            else:
                self.low[u] = min(self.low[u], self.disc[v])

        if parent == -1 and children > 1:
            self.articulation_points.add(u)


if __name__ == "__main__":
    n = 6
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (4, 5)]

    finder = BridgeFinder(n, edges)
    bridges, articulation_points = finder.run()

    print("Bridges:", bridges)
    print("Articulation points:", articulation_points)
