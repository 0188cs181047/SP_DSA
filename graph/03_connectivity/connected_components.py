"""
Count Connected Components in an Undirected Graph   (Difficulty: Medium)
Asked at: Google, Meta, Amazon

Problem:
Given n nodes (0 to n-1) and a list of undirected edges, count how many
separate connected components exist — groups of nodes reachable from
each other, with no edges connecting different groups.

Example:
    n = 6
    edges = [(0, 1), (1, 2), (3, 4)]

Flow diagram:
    0 --- 1 --- 2        3 --- 4        5

    Component 1: {0, 1, 2}
    Component 2: {3, 4}
    Component 3: {5}      <- isolated node, still its own component

    Answer: 3

Approach (two common ways — know both, interviewers ask for either):
1. DFS/BFS: for every unvisited node, run a traversal marking everything
   reachable as visited; each traversal you start = one new component.
2. Union-Find: union every edge's two endpoints, then count the number
   of distinct roots. Better when edges arrive as a stream / need to
   answer "are these two connected?" repeatedly.

Time Complexity:  O(V + E) for DFS/BFS; ~O((V + E) * α(V)) for Union-Find.
Space Complexity: O(V + E)
"""

from collections import defaultdict


def count_components_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    components = 0
    for node in range(n):
        if node not in visited:
            components += 1
            dfs(node)

    return components


def count_components_union_find(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression
            x = parent[x]
        return x

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for u, v in edges:
        union(u, v)

    return len({find(node) for node in range(n)})


if __name__ == "__main__":
    n = 6
    edges = [(0, 1), (1, 2), (3, 4)]

    print("Components (DFS):", count_components_dfs(n, edges))
    print("Components (Union-Find):", count_components_union_find(n, edges))
