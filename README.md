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
├── array/                # Two pointers, sliding window, prefix sum, Kadane's, and more
├── linked_list/          # Singly linked list basics, reversal, cycles, merging, LRU Cache
├── stack/                # LIFO basics, monotonic stack, expression evaluation
├── queue/                # FIFO basics, deque patterns, BFS applications
├── tree/                 # Binary tree structure checks, height/BST/views, serialization
│   └── (traversal.py — Preorder/Inorder/Postorder/Level Order — lives in ../searching/)
├── graph/                # Adjacency list/matrix, BFS/DFS, shortest paths, MST, SCC
├── hash_table/           # Hashing, collisions, frequency counting, membership
├── searching/            # Linear/binary search and its variants, binary search on the answer
├── sorting/              # Bubble/insertion/merge/quick/heap/counting sort, related problems
├── dynamic_programming/  # Memoization, tabulation, knapsack family, grid DP
└── logical/              # Aptitude-style logic/number puzzles (FizzBuzz, GCD, bit tricks, etc.)
```

Every folder has its own `README.md` with definitions, diagrams, and time/space
complexity for the topic, plus an **Interview Roadmap (Basic → Advanced)** table —
every problem, its pattern, difficulty, and which companies (FAANG/big tech and
MNCs like TCS/Infosys/Wipro) commonly ask it — linking to a runnable `.py` file
for each one.

## Summary

> DSA is about picking the right data structure, designing an efficient algorithm around it, and analyzing the time/space trade-offs so the solution stays correct and fast as the input grows.
