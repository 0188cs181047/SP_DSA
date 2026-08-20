"""
Shortest Path in an Unweighted Graph (BFS)   (Difficulty: Medium)
Asked at: Amazon, Microsoft

Problem:
Given an unweighted graph and a source node, find the shortest distance
(fewest edges) from source to every other node.

Example graph:
    0 --- 1 --- 3
    |           |
    2 --------- +

Flow diagram (BFS layers from 0):
    Layer 0: [0]              dist[0] = 0
    Layer 1: [1, 2]           dist[1] = dist[2] = 1
    Layer 2: [3]              dist[3] = 2   (via 1 or via 2, both length 2)

Approach:
- BFS naturally explores nodes in order of distance from the source
  because it processes level by level. The FIRST time you reach a node,
  that's its shortest distance (in an unweighted graph).
- This breaks for weighted graphs — that's why weighted shortest path
  needs Dijkstra instead (see dijkstra.py).

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import defaultdict, deque


def shortest_path_bfs(graph, source, n):
    dist = [-1] * n
    dist[source] = 0
    queue = deque([source])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


if __name__ == "__main__":
    n = 4
    graph = defaultdict(list, {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2],
    })

    print("Shortest distances from node 0:", shortest_path_bfs(graph, 0, n))
