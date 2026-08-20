"""
Dijkstra's Algorithm — Shortest Path (Non-Negative Weights)   (Difficulty: Medium/Hard)
Asked at: Google, Uber, Amazon, Ola — routing/maps-style companies love this

Problem:
Given a weighted graph (all weights >= 0) and a source node, find the
shortest distance from source to every other node.

Example graph:
        (4)
    0 -------- 1
    |          |
   (1)        (2)
    |          |
    2 -------- 3
        (5)

Flow (min-heap driven relaxation):
    dist = {0: 0, 1: inf, 2: inf, 3: inf}
    pop (0, node=0)  -> relax 1 (0+4=4), relax 2 (0+1=1)
    pop (1, node=2)  -> relax 3 (1+5=6)
    pop (4, node=1)  -> relax 3 (4+2=6, no improvement)
    pop (6, node=3)  -> done

    Final: dist = {0: 0, 1: 4, 2: 1, 3: 6}

Approach:
- Greedy + min-heap: always expand the closest not-yet-finalized node.
- Maintain dist[] initialized to infinity except source = 0.
- Pop the smallest-distance node from the heap; for each neighbor, if
  going through this node gives a shorter path ("relaxation"), update
  it and push the new distance.
- Skip stale heap entries (a node can be pushed multiple times with
  different distances — only the smallest one matters).
- Does NOT work with negative edge weights (use Bellman-Ford instead).

Time Complexity:  O((V + E) log V) with a binary heap.
Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict


def dijkstra(graph, source, n):
    dist = [float("inf")] * n
    dist[source] = 0
    min_heap = [(0, source)]

    while min_heap:
        current_dist, node = heapq.heappop(min_heap)

        if current_dist > dist[node]:
            continue  # stale entry, a shorter path was already found

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist


if __name__ == "__main__":
    n = 4
    graph = defaultdict(list, {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (3, 2)],
        2: [(0, 1), (3, 5)],
        3: [(1, 2), (2, 5)],
    })

    print("Shortest distances from node 0:", dijkstra(graph, 0, n))
