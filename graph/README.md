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

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
an ASCII flow diagram, the approach, and time/space complexity in its
docstring. Work through them top to bottom — each section builds on the one
before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_representation](01_representation) | Build a Graph | [build_graph.py](01_representation/build_graph.py) | Adjacency List / Matrix | Easy | Amazon, Google, Microsoft |
| 2 | [02_traversal](02_traversal) | BFS Traversal | [bfs_traversal.py](02_traversal/bfs_traversal.py) | BFS | Easy | Amazon, Microsoft |
| 3 | [02_traversal](02_traversal) | DFS Traversal | [dfs_traversal.py](02_traversal/dfs_traversal.py) | DFS | Easy | Amazon, Adobe |
| 4 | [03_connectivity](03_connectivity) | Number of Islands | [number_of_islands.py](03_connectivity/number_of_islands.py) | Grid DFS/BFS | Medium | Amazon, Google, Meta |
| 5 | [03_connectivity](03_connectivity) | Flood Fill | [flood_fill.py](03_connectivity/flood_fill.py) | Grid DFS/BFS | Easy | Google, Amazon |
| 6 | [03_connectivity](03_connectivity) | Connected Components | [connected_components.py](03_connectivity/connected_components.py) | DFS/BFS, Union-Find | Medium | Google, Meta |
| 7 | [04_cycle_detection](04_cycle_detection) | Cycle in Undirected Graph | [detect_cycle_undirected.py](04_cycle_detection/detect_cycle_undirected.py) | DFS + parent, Union-Find | Medium | Amazon, Microsoft |
| 8 | [04_cycle_detection](04_cycle_detection) | Cycle in Directed Graph | [detect_cycle_directed.py](04_cycle_detection/detect_cycle_directed.py) | 3-color DFS | Medium | Amazon, Google |
| 9 | [05_topological_sort](05_topological_sort) | Topological Sort | [topological_sort.py](05_topological_sort/topological_sort.py) | Kahn's BFS, DFS+Stack | Medium | Amazon, Google |
| 10 | [05_topological_sort](05_topological_sort) | Course Schedule I & II | [course_schedule.py](05_topological_sort/course_schedule.py) | Topological Sort | Medium | Google, Meta, Amazon |
| 11 | [06_shortest_path](06_shortest_path) | Shortest Path (Unweighted) | [shortest_path_bfs.py](06_shortest_path/shortest_path_bfs.py) | BFS | Medium | Amazon, Microsoft |
| 12 | [06_shortest_path](06_shortest_path) | Dijkstra's Algorithm | [dijkstra.py](06_shortest_path/dijkstra.py) | Greedy + Min-Heap | Medium/Hard | Google, Uber, Amazon |
| 13 | [06_shortest_path](06_shortest_path) | Bellman-Ford | [bellman_ford.py](06_shortest_path/bellman_ford.py) | Edge Relaxation | Hard | Google, Bloomberg |
| 14 | [06_shortest_path](06_shortest_path) | Floyd-Warshall | [floyd_warshall.py](06_shortest_path/floyd_warshall.py) | DP, All-Pairs | Hard | Bloomberg, Google |
| 15 | [07_union_find_mst](07_union_find_mst) | Union-Find (DSU) | [union_find.py](07_union_find_mst/union_find.py) | Path Compression + Rank | Medium | Google, Meta, Amazon |
| 16 | [07_union_find_mst](07_union_find_mst) | Kruskal's MST | [kruskal_mst.py](07_union_find_mst/kruskal_mst.py) | Greedy + Union-Find | Hard | Google, Bloomberg |
| 17 | [07_union_find_mst](07_union_find_mst) | Prim's MST | [prim_mst.py](07_union_find_mst/prim_mst.py) | Greedy + Min-Heap | Hard | Google, Bloomberg |
| 18 | [08_advanced](08_advanced) | Clone Graph | [clone_graph.py](08_advanced/clone_graph.py) | DFS/BFS + HashMap | Medium | Google, Meta, Amazon |
| 19 | [08_advanced](08_advanced) | Is Graph Bipartite? | [bipartite_check.py](08_advanced/bipartite_check.py) | 2-Coloring (BFS) | Medium | Meta, Google |
| 20 | [08_advanced](08_advanced) | Word Ladder | [word_ladder.py](08_advanced/word_ladder.py) | Implicit Graph + BFS | Hard | Amazon, Google, LinkedIn |
| 21 | [08_advanced](08_advanced) | Bridges & Articulation Points | [bridges_and_articulation_points.py](08_advanced/bridges_and_articulation_points.py) | Tarjan's (disc/low) | Hard | Google, Bloomberg |
| 22 | [08_advanced](08_advanced) | Strongly Connected Components | [strongly_connected_components.py](08_advanced/strongly_connected_components.py) | Kosaraju's Algorithm | Hard | Google, Uber |

## How to Pick the Right Algorithm in an Interview

When you hear a new graph question, match its clues against this flow instead
of guessing:

```
                    Is the input a grid (matrix of cells)?
                         |                        |
                        yes                       no
                         |                         |
              Treat cells as nodes,        Do you need to VISIT every
              4/8-directional moves           reachable node, or find
              as edges -> DFS/BFS               a PATH/DISTANCE?
              (Islands, Flood Fill)                    |
                                        -------------------------------
                                        |                             |
                                Just visit / count            Need a distance / path
                                (Connected Components)                 |
                                                        --------------------------------
                                                        |                              |
                                                Unweighted graph?              Weighted graph?
                                                        |                              |
                                                  BFS (shortest_path_bfs)    All-Pairs? -> Floyd-Warshall
                                                                             Negative edges? -> Bellman-Ford
                                                                             Else -> Dijkstra

                    Does the graph have DIRECTION (dependencies)?
                                         |
                                        yes
                                         |
                          Need an ORDER that respects dependencies?
                                 |                        |
                                yes                       no
                                 |                         |
                     Topological Sort / Course       Just check for a cycle?
                     Schedule (Kahn's / DFS+Stack)     -> 3-color DFS

                    Need to know which edges/nodes are "critical" (single point
                    of failure)?  -> Bridges & Articulation Points (Tarjan's)

                    Need mutually-reachable groups in a DIRECTED graph?
                    -> Strongly Connected Components (Kosaraju's)

                    Need to connect everything as CHEAPLY as possible
                    (no cycles, minimize total weight)?
                    -> Minimum Spanning Tree: Kruskal's (sort edges) or
                       Prim's (grow from a node)

                    Need to check "are these two nodes in the same group?"
                    repeatedly, or as edges stream in?  -> Union-Find
```

## Folder Structure

```
graph/
├── README.md
├── 01_representation/       # How to build a graph in code
├── 02_traversal/             # BFS, DFS
├── 03_connectivity/          # Islands, Flood Fill, Connected Components
├── 04_cycle_detection/       # Undirected & directed cycle detection
├── 05_topological_sort/      # Kahn's, DFS+Stack, Course Schedule
├── 06_shortest_path/         # BFS, Dijkstra, Bellman-Ford, Floyd-Warshall
├── 07_union_find_mst/        # Union-Find, Kruskal's, Prim's
└── 08_advanced/              # Clone Graph, Bipartite, Word Ladder,
                               # Bridges/Articulation Points, SCC
```

Run any file directly to see it work, e.g.:

```bash
python 06_shortest_path/dijkstra.py
```
