"""
Detect Cycle in a Directed Graph   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
Given a directed graph, determine whether it contains a cycle. This is
the core check behind "Course Schedule" style problems: if prerequisites
form a cycle, the courses are impossible to finish.

Example (has a cycle):
    0 -> 1 -> 2
         ^    |
         |    v
         +--- 3

    1 -> 2 -> 3 -> 1   <- cycle!

Approach — 3-color DFS (the standard interview answer):
- WHITE (0): not visited yet
- GRAY  (1): currently on the recursion stack (an ancestor in this DFS path)
- BLACK (2): fully processed, done with all its descendants

A cycle exists if DFS ever reaches a GRAY node — that means we've looped
back to a node that is still one of our own ancestors on the current path.
Reaching a BLACK node is fine (just a shared descendant, not a cycle).

Flow:
    dfs(0): color[0]=GRAY -> visit 1
      dfs(1): color[1]=GRAY -> visit 2
        dfs(2): color[2]=GRAY -> visit 3
          dfs(3): color[3]=GRAY -> visit 1 -> color[1] is GRAY -> CYCLE!

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict

WHITE, GRAY, BLACK = 0, 1, 2


def has_cycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for node in range(n):
        if color[node] == WHITE:
            if dfs(node):
                return True

    return False


if __name__ == "__main__":
    n = 4
    cyclic_edges = [(0, 1), (1, 2), (2, 3), (3, 1)]
    acyclic_edges = [(0, 1), (1, 2), (2, 3)]

    print("Has cycle (cyclic graph):", has_cycle(n, cyclic_edges))
    print("Has cycle (acyclic graph, a DAG):", has_cycle(n, acyclic_edges))
