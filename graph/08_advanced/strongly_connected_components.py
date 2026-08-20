"""
Strongly Connected Components — Kosaraju's Algorithm   (Difficulty: Hard)
Asked at: Google, Uber

Problem:
In a DIRECTED graph, a Strongly Connected Component (SCC) is a maximal
group of nodes where every node can reach every other node in the group
via directed edges. Find all SCCs.

Example:
    0 -> 1 -> 2 -> 0     3 -> 4
              |          ^
              +----------+

Flow diagram:
    SCC #1: {0, 1, 2}   -- 0->1->2->0 forms a cycle, all mutually reachable
    SCC #2: {3}          -- 3 can reach 4 but 4 cannot reach back to 3
    SCC #3: {4}

Approach — Kosaraju's Algorithm (3 passes):
1. Run DFS on the original graph, pushing each node onto a stack in
   postorder (finish-time order) — same idea as topological sort.
2. Reverse every edge in the graph (transpose graph).
3. Pop nodes off the stack one at a time; for each unvisited node, run
   DFS on the TRANSPOSED graph — everything reached in this one DFS call
   is exactly one SCC.

Why it works (intuition): the node finished LAST in step 1 is a "source"
that can reach the most nodes. Running DFS from it on the reversed graph
only reaches nodes that could ALSO reach it originally — that's the
definition of mutual reachability.

Time Complexity:  O(V + E) — 3 linear passes.
Space Complexity: O(V + E)
"""

from collections import defaultdict


def find_sccs(n, edges):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = set()
    finish_stack = []

    def dfs_fill_order(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_fill_order(neighbor)
        finish_stack.append(node)

    for node in range(n):
        if node not in visited:
            dfs_fill_order(node)

    visited.clear()
    sccs = []

    def dfs_collect(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in reverse_graph[node]:
            if neighbor not in visited:
                dfs_collect(neighbor, component)

    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            component = []
            dfs_collect(node, component)
            sccs.append(component)

    return sccs


if __name__ == "__main__":
    n = 5
    edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3)]

    print("Strongly Connected Components:", find_sccs(n, edges))
