"""
Bellman-Ford Algorithm — Shortest Path with Negative Weights   (Difficulty: Hard)
Asked at: Google, Bloomberg — financial/arbitrage-style graph problems

Problem:
Given a weighted directed graph (weights CAN be negative) and a source,
find the shortest distance to every node, and detect negative-weight
cycles (which make "shortest path" undefined — you could loop forever
to keep decreasing the distance).

Example graph:
    0 --(4)--> 1
    0 --(5)--> 2
    1 --(-3)-> 2   <- negative edge, Dijkstra would get this wrong

Flow (relax every edge, n-1 times):
    Iteration 1: dist[1] = 4, dist[2] = min(5, 4-3) = 1
    Iteration 2: no more improvements -> converged after V-1 rounds
    Iteration 3 (the extra check): if ANYTHING still improves,
                                    there's a negative cycle

Approach:
- Relax every edge (u, v, w): if dist[u] + w < dist[v], update dist[v].
- Do this for V-1 rounds — a shortest path visits at most V-1 edges (in
  a graph with no negative cycle), so V-1 rounds guarantees convergence.
- Run one MORE round after that: if any edge still relaxes, a negative
  cycle exists and shortest paths are not well-defined.
- Unlike Dijkstra, works correctly with negative edges — but is slower.

Time Complexity:  O(V * E)
Space Complexity: O(V)
"""

def bellman_ford(n, edges, source):
    """edges = [(u, v, weight), ...]"""
    dist = [float("inf")] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist


if __name__ == "__main__":
    n = 3
    edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3)]

    print("Shortest distances from node 0:", bellman_ford(n, edges, 0))

    negative_cycle_edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
    try:
        bellman_ford(3, negative_cycle_edges, 0)
    except ValueError as e:
        print("Detected:", e)
