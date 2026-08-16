# Queue

A **Queue** is a linear data structure that follows **FIFO (First In, First Out)** order — the first element added is the first one removed. Think of a line at a ticket counter: whoever joins first gets served first.

```
enqueue -> [ 1 | 2 | 3 | 4 ] -> dequeue
           front         rear
```

## Core Operations

| Operation | Description | Time Complexity |
|---|---|---|
| `enqueue(x)` | Add element `x` to the rear | O(1) |
| `dequeue()` | Remove and return the front element | O(1) |
| `peek()` / `front()` | Look at the front element without removing it | O(1) |
| `is_empty()` | Check if the queue has no elements | O(1) |

Note: a naive array-based queue where `dequeue` removes index 0 is O(n) (everything shifts). Efficient implementations use a **circular buffer**, a **linked list** (head/tail pointers), or `collections.deque` in Python, all giving O(1) `enqueue`/`dequeue`.

## Types

| Type | Description |
|---|---|
| Simple Queue | Standard FIFO queue |
| Circular Queue | Rear wraps around to reuse freed space at the front, avoiding wasted array slots |
| Deque (Double-Ended Queue) | Insert/remove from both front and rear |
| Priority Queue | Elements are dequeued by priority, not insertion order (usually backed by a Heap) |

## When to Use a Queue

- Order of processing must match order of arrival.
- Task scheduling, print job spooling, request handling (rate limiting/buffering).
- **BFS traversal** of trees and graphs — the queue is what makes BFS "level by level."
- Producer-consumer patterns / message queues.

## Common Problems Solved with Queues

- Level Order Traversal of a tree (see [tree/traversal.py](../tree/traversal.py))
- Breadth-First Search (BFS) on a graph
- Implementing a stack using two queues (and vice versa)
- Sliding window maximum (using a deque)
- Task/CPU scheduling simulations
