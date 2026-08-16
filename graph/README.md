# Graph

A **Graph** is a non-linear data structure made up of a set of **vertices (nodes)** connected by **edges**. Unlike a tree, a graph can have cycles and doesn't need a single root — any node can connect to any other node.

```
    A --- B
    |     |
    C --- D --- E
```

## Key Terms

| Term | Meaning |
|---|---|
| Vertex (Node) | A single point in the graph |
| Edge | A connection between two vertices |
| Directed Graph | Edges have a direction, `A -> B` doesn't imply `B -> A` |
| Undirected Graph | Edges go both ways, `A - B` means connected both ways |
| Weighted Graph | Edges carry a cost/weight (e.g. distance, time) |
| Cycle | A path that starts and ends at the same vertex |
| Degree | Number of edges connected to a vertex |

## Representations

| Representation | Description | Space | Edge Lookup |
|---|---|---|---|
| Adjacency Matrix | 2D matrix, `matrix[i][j] = 1` if edge exists | O(V²) | O(1) |
| Adjacency List | Each vertex stores a list of its neighbors | O(V + E) | O(degree of v) |

Adjacency List is preferred for sparse graphs (most real-world graphs); Adjacency Matrix is simpler for dense graphs or when O(1) edge lookup matters.

## Traversal

| Traversal | Data Structure Used | Description |
|---|---|---|
| BFS (Breadth-First Search) | Queue | Explores neighbors level by level; finds shortest path in unweighted graphs |
| DFS (Depth-First Search) | Stack / Recursion | Explores as deep as possible before backtracking |

## Common Algorithms

| Algorithm | Purpose | Complexity |
|---|---|---|
| BFS / DFS | Traversal, connectivity, cycle detection | O(V + E) |
| Dijkstra's Algorithm | Shortest path (non-negative weights) | O((V + E) log V) with a min-heap |
| Bellman-Ford | Shortest path (handles negative weights) | O(V * E) |
| Kruskal's / Prim's | Minimum Spanning Tree | O(E log V) |
| Topological Sort | Ordering for Directed Acyclic Graphs (DAGs) | O(V + E) |
| Union-Find (Disjoint Set) | Cycle detection, connected components | ~O(α(n)) per operation |

## When to Use Graphs

- Modeling relationships/networks: social networks, road maps, web page links, dependency trees.
- Finding shortest/cheapest paths (navigation, routing).
- Detecting cycles or checking connectivity (e.g. deadlock detection, network reliability).
- Scheduling with dependencies (topological sort — e.g. build systems, course prerequisites).

## Common Problems Solved with Graphs

- Number of Islands (grid as an implicit graph, DFS/BFS)
- Shortest Path (Dijkstra, BFS for unweighted)
- Course Schedule (cycle detection + topological sort)
- Clone a Graph
- Connected Components / Union-Find
