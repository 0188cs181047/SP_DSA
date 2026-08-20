"""
Graph Representation — Adjacency List vs Adjacency Matrix   (Difficulty: Easy)
Asked at: Amazon, Microsoft, Google (almost every graph interview starts here)

Problem:
Before solving any graph problem you must be able to *build* a graph from
raw input (usually a list of edges) and choose the right representation.
Interviewers often start with "How would you represent this graph in code?"
to see if you understand the space/time trade-offs.

Example edge list (undirected):
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

Flow diagram:
    0 --- 1
    |     |
    2 --- +
    |
    3

Adjacency List (preferred for sparse graphs):
    0: [1, 2]
    1: [0, 2]
    2: [0, 1, 3]
    3: [2]

Adjacency Matrix (preferred for dense graphs / O(1) edge lookup):
        0  1  2  3
    0 [ 0  1  1  0 ]
    1 [ 1  0  1  0 ]
    2 [ 1  1  0  1 ]
    3 [ 0  0  1  0 ]

Approach:
- Adjacency List: dict/list of lists. Each edge (u, v) appends v to u's list
  (and u to v's list if undirected). Uses O(V + E) space.
- Adjacency Matrix: V x V grid, matrix[u][v] = 1 marks an edge.
  Uses O(V^2) space regardless of how many edges actually exist.

Time Complexity:  O(V + E) to build the list, O(V^2) to build the matrix.
Space Complexity: O(V + E) for the list, O(V^2) for the matrix.
"""

from collections import defaultdict


def build_adjacency_list(n, edges, directed=False):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    for node in range(n):
        graph.setdefault(node, [])
    return dict(graph)


def build_adjacency_matrix(n, edges, directed=False):
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix


def build_weighted_adjacency_list(n, edges, directed=False):
    """edges = [(u, v, weight), ...]"""
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    for node in range(n):
        graph.setdefault(node, [])
    return dict(graph)


if __name__ == "__main__":
    n = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

    print("Adjacency List:")
    print(build_adjacency_list(n, edges))

    print("\nAdjacency Matrix:")
    for row in build_adjacency_matrix(n, edges):
        print(row)

    print("\nWeighted Adjacency List:")
    weighted_edges = [(0, 1, 4), (0, 2, 1), (1, 2, 2), (2, 3, 5)]
    print(build_weighted_adjacency_list(n, weighted_edges))
