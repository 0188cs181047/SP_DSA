"""
Detect Cycle in an Undirected Graph   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Adobe

Problem:
Given an undirected graph, determine whether it contains a cycle — a
path that revisits a node without immediately going back the way it came.

Example (has a cycle):
    0 --- 1
    |     |
    2 --- 3

    0 -> 1 -> 3 -> 2 -> 0   <- cycle!

Example (no cycle — a tree):
    0 --- 1
    |
    2 --- 3

Flow (DFS with parent tracking):
    dfs(0, parent=-1) -> visit 1
      dfs(1, parent=0) -> visit 3
        dfs(3, parent=1) -> visit 2
          dfs(2, parent=3) -> neighbor 0 is visited AND is not parent(3)
                              -> CYCLE FOUND

Approach:
- In an undirected graph, every edge is stored both ways, so a DFS will
  immediately see the node it just came from — that does NOT count as a
  cycle. Track the parent; if you reach an already-visited node that is
  NOT your immediate parent, you've found a genuine cycle.
- Alternative: Union-Find — if both endpoints of an edge already share
  the same root before you union them, adding that edge creates a cycle.

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict


def has_cycle_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


def has_cycle_union_find(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        root_u, root_v = find(u), find(v)
        if root_u == root_v:
            return True
        parent[root_u] = root_v

    return False


if __name__ == "__main__":
    n = 4
    cyclic_edges = [(0, 1), (1, 3), (3, 2), (2, 0)]
    acyclic_edges = [(0, 1), (0, 2), (2, 3)]

    print("Has cycle (cyclic graph):", has_cycle_dfs(n, cyclic_edges))
    print("Has cycle (acyclic graph):", has_cycle_dfs(n, acyclic_edges))
    print("Has cycle via Union-Find:", has_cycle_union_find(n, cyclic_edges))
