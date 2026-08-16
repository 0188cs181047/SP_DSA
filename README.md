# DSA — Data Structures & Algorithms

DSA (**Data Structures and Algorithms**) is the study of organizing data efficiently and designing step-by-step procedures (algorithms) to solve problems — then analyzing how well those solutions scale as input size grows.

Choosing the right data structure and algorithm is what separates code that works from code that works *well*. For example, searching for an item in a list takes O(n) time, but searching in a hash table takes O(1) on average — that difference matters a lot once your data grows from 100 items to 100 million.

## 1. Data Structures

A **data structure** is a way of organizing and storing data so it can be accessed and modified efficiently.

| Data Structure | Description | Common Use Case |
|---|---|---|
| Array | Fixed-size, contiguous, indexed collection | Fast random access |
| Linked List | Nodes connected via pointers | Frequent insertions/deletions |
| Stack | Last-In-First-Out (LIFO) | Undo history, function calls |
| Queue | First-In-First-Out (FIFO) | Task scheduling, buffering |
| Hash Table | Key-value storage using a hash function | Fast lookups |
| Tree | Hierarchical structure of connected nodes | Sorted data, hierarchies |
| Graph | Nodes connected by edges (not necessarily hierarchical) | Networks, maps, relationships |

## 2. Algorithms

An **algorithm** is a step-by-step procedure for solving a computational problem.

Common categories:
- **Searching** — Linear Search, Binary Search
- **Sorting** — Bubble Sort, Merge Sort, Quick Sort
- **Tree Traversal** — Preorder, Inorder, Postorder, Level Order
- **Graph Traversal** — BFS, DFS
- **Dynamic Programming** — Breaking problems into overlapping subproblems

## 3. Complexity Analysis

Complexity analysis measures how an algorithm's time and memory usage grow as the input size (`n`) increases. It's expressed using **Big O notation**.

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Accessing an array element by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Looping through an array once |
| O(n log n) | Linearithmic | Merge sort, Quick sort |
| O(n²) | Quadratic | Bubble sort, nested loops |

Two things are usually measured:
- **Time complexity** — how the runtime grows with input size
- **Space complexity** — how much extra memory the algorithm needs

## Repository Structure

```
SP_DSA/
├── array/               # Static/dynamic arrays, complexity, common problems
├── linked_list/          # Singly/doubly/circular linked lists
├── stack/               # LIFO structure, array & linked-list based
├── queue/               # FIFO structure, circular queue, deque, priority queue
├── tree/                 # Binary tree concepts and implementations
│   ├── traversal.py            # Preorder, Inorder, Postorder, Level Order
│   ├── full_binary_tree.py     # Every node has 0 or 2 children
│   ├── complete_binary_tree.py # Filled left-to-right, last level may be partial
│   ├── perfect_binary_tree.py  # All internal nodes have 2 children, all leaves same depth
│   └── balance_binary_tree.py  # Left/right subtree height differs by at most 1
├── graph/                # Adjacency list/matrix, BFS/DFS, shortest paths
├── hash_table/           # Hashing, collisions, key-value lookups
├── searching/            # Linear search, binary search
├── sorting/              # Bubble/insertion/merge/quick/heap sort
└── dynamic_programming/  # Memoization, tabulation, classic DP problems
```

Every folder has its own `README.md` with definitions, diagrams, time/space complexity, and common interview problems for that topic.

## Summary

> DSA is about picking the right data structure, designing an efficient algorithm around it, and analyzing the time/space trade-offs so the solution stays correct and fast as the input grows.
