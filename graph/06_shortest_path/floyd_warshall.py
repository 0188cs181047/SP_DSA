"""
Floyd-Warshall Algorithm — All-Pairs Shortest Path   (Difficulty: Hard)
Asked at: Bloomberg, Google

Problem:
Given a weighted graph, find the shortest distance between EVERY pair of
nodes (not just from one source). Works with negative edges, as long as
there's no negative cycle.

Example graph (adjacency matrix, inf = no direct edge):
        0    1    2
    0 [ 0,   3,  inf]
    1 [ 8,   0,   2 ]
    2 [ 5,  inf,  0 ]

Flow (try every node k as an intermediate "stepping stone"):
    Using k=0: dist[2][1] = min(inf, dist[2][0] + dist[0][1]) = min(inf, 5+3) = 8
    Using k=1: dist[0][2] = min(inf, dist[0][1] + dist[1][2]) = min(inf, 3+2) = 5
    Using k=2: dist[1][0] = min(8,   dist[1][2] + dist[2][0]) = min(8, 2+5)   = 7

    Final shortest distances between ALL pairs computed in one pass.

Approach:
- Dynamic programming: dist[i][j] = shortest path from i to j using only
  the first k nodes as intermediates.
- Triple nested loop: for every intermediate k, for every pair (i, j),
  check if going i -> k -> j is shorter than the current i -> j.
- Simple to code (3 loops), which is why it's preferred over running
  Dijkstra V times when the graph is small/dense or has negative edges.

Time Complexity:  O(V^3)
Space Complexity: O(V^2)
"""

def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    INF = float("inf")
    matrix = [
        [0,   3,   INF],
        [8,   0,   2],
        [5,   INF, 0],
    ]

    result = floyd_warshall(matrix)
    for row in result:
        print(row)
