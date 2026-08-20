"""
Topological Sort (Kahn's BFS + DFS)   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
Given a Directed Acyclic Graph (DAG), produce a linear ordering of nodes
such that for every directed edge u -> v, u comes before v. Classic use
case: ordering tasks that have prerequisites.

Example:
    5 -> 0     4 -> 0
    5 -> 2     4 -> 1
    2 -> 3
    3 -> 1

Flow diagram:
    5 --> 2 --> 3 --> 1
    |            ^     ^
    v            |     |
    0            4 ----+

    Valid ordering: 5, 4, 2, 3, 1, 0  (multiple valid orderings can exist)

Approach A — Kahn's Algorithm (BFS, easier to explain in interviews):
1. Compute in-degree (number of incoming edges) for every node.
2. Push all nodes with in-degree 0 into a queue (no prerequisites).
3. Pop a node, add to result, decrement in-degree of its neighbors.
4. If a neighbor's in-degree hits 0, push it.
5. If result has fewer than n nodes at the end, the graph has a cycle.

Approach B — DFS + Stack:
1. DFS from every unvisited node; after visiting all of a node's
   neighbors, push the node onto a stack (postorder).
2. Reverse the stack — that's a valid topological order.

Time Complexity:  O(V + E) for both approaches.
Space Complexity: O(V + E)
"""

from collections import defaultdict, deque


def topo_sort_kahn(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque(node for node in range(n) if in_degree[node] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != n:
        raise ValueError("Graph has a cycle — no valid topological order")

    return order


def topo_sort_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in range(n):
        if node not in visited:
            dfs(node)

    return stack[::-1]


if __name__ == "__main__":
    n = 6
    edges = [(5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1)]

    print("Topological order (Kahn's/BFS):", topo_sort_kahn(n, edges))
    print("Topological order (DFS):", topo_sort_dfs(n, edges))
