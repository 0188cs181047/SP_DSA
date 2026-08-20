"""
BFS Traversal of a Graph   (Difficulty: Easy)
Asked at: Amazon, Microsoft, Flipkart

Problem:
Given a graph and a starting node, visit every reachable node level by
level (all neighbors of the start before any neighbor-of-neighbor).

Example graph:
    0 --- 1
    |     |
    2 --- 3 --- 4

Starting BFS from 0:
    Level 0: [0]
    Level 1: [1, 2]
    Level 2: [3]
    Level 3: [4]
    Visit order: 0 -> 1 -> 2 -> 3 -> 4

Flow:
    queue = [0]
    visited = {0}

    pop 0 -> visit -> push unvisited neighbors 1, 2   queue=[1,2]
    pop 1 -> visit -> push unvisited neighbor 3        queue=[2,3]
    pop 2 -> visit -> 3 already queued                 queue=[3]
    pop 3 -> visit -> push unvisited neighbor 4         queue=[4]
    pop 4 -> visit -> no new neighbors                  queue=[]

Approach:
- Use a queue (FIFO). Mark start visited, push it.
- While queue not empty: pop front, record it, push all unvisited
  neighbors and mark them visited *at push time* (not at pop time) to
  avoid pushing the same node twice.

Time Complexity:  O(V + E) — every vertex and edge is processed once.
Space Complexity: O(V) — visited set + queue.
"""

from collections import deque, defaultdict


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    graph = defaultdict(list, {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3],
    })

    print("BFS from 0:", bfs(graph, 0))
