"""
DFS Traversal of a Graph   (Difficulty: Easy)
Asked at: Amazon, Microsoft, Adobe

Problem:
Given a graph and a starting node, visit every reachable node by going
as deep as possible before backtracking.

Example graph:
    0 --- 1
    |     |
    2 --- 3 --- 4

DFS from 0 (visiting neighbors in list order):
    0 -> 1 -> 3 -> 2 -> 4
                (backtrack from 2, no new node)
                (backtrack to 3 -> visit 4)

Flow (recursive call stack):
    dfs(0) -> dfs(1) -> dfs(3) -> dfs(2) [2's neighbors already visited, return]
                              -> dfs(4) [4's neighbors already visited, return]

Approach:
- Recursive: mark node visited, recurse into every unvisited neighbor.
- Iterative: use an explicit stack instead of the call stack (handles very
  deep graphs where recursion could hit Python's recursion limit).

Time Complexity:  O(V + E)
Space Complexity: O(V) — visited set + recursion/explicit stack.
"""

from collections import defaultdict


def dfs_recursive(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []

    visited.add(start)
    order.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

    return order


def dfs_iterative(graph, start):
    visited = {start}
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order


if __name__ == "__main__":
    graph = defaultdict(list, {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3],
    })

    print("DFS (recursive) from 0:", dfs_recursive(graph, 0))
    print("DFS (iterative) from 0:", dfs_iterative(graph, 0))
