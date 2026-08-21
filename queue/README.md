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

- Level Order Traversal of a tree (see [searching/traversal.py](../searching/traversal.py))
- Breadth-First Search (BFS) on a graph
- Implementing a stack using two queues (and vice versa)
- Sliding window maximum (using a deque)
- Task/CPU scheduling simulations

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_basics](01_basics) | Design a Circular Queue | [circular_queue.py](01_basics/circular_queue.py) | Fixed Array + Modulo | Easy | TCS, Amazon |
| 2 | [01_basics](01_basics) | Implement a Stack Using Queues | [stack_using_queues.py](01_basics/stack_using_queues.py) | Single Queue Rotation | Easy/Medium | Amazon, Microsoft |
| 3 | [02_deque](02_deque) | Sliding Window Maximum | [sliding_window_maximum.py](02_deque/sliding_window_maximum.py) | Monotonic Deque | Hard | Amazon, Google, Meta |
| 4 | [02_deque](02_deque) | First Negative Number in Every Window of Size K | [first_negative_in_window.py](02_deque/first_negative_in_window.py) | Deque of Indices | Medium | Amazon, Adobe |
| 5 | [03_bfs_applications](03_bfs_applications) | Rotting Oranges (Multi-source BFS) | [rotten_oranges.py](03_bfs_applications/rotten_oranges.py) | Multi-source BFS | Medium | Amazon, Google, Microsoft |
| 6 | [03_bfs_applications](03_bfs_applications) | Generate Binary Numbers from 1 to N | [generate_binary_numbers.py](03_bfs_applications/generate_binary_numbers.py) | BFS-style Generation | Easy | Amazon |
| 7 | [04_advanced](04_advanced) | Design a Hit Counter (last 5 minutes) | [design_hit_counter.py](04_advanced/design_hit_counter.py) | Queue of Timestamps | Medium | Google, Amazon |
| 8 | [04_advanced](04_advanced) | Task Scheduler with Cooldown | [task_scheduler.py](04_advanced/task_scheduler.py) | Greedy + Heap/Queue | Medium | Amazon, Meta, Uber |

## How to Pick the Right Pattern in an Interview

- Need strict FIFO order for scheduling/buffering? → **Simple / Circular Queue**
- Need the max or min over a sliding window efficiently? → **Monotonic Deque**
- Need to expand outward level-by-level from one or more sources (grid or graph)? → **BFS with a queue**
- Need to track events within a trailing time window? → **Queue of timestamps**, popping expired entries from the front

## Folder Structure

```
queue/
├── README.md
├── 01_basics/            # Circular Queue, Stack Using Queues
├── 02_deque/             # Sliding Window Maximum, First Negative in Window
├── 03_bfs_applications/  # Rotten Oranges, Generate Binary Numbers
└── 04_advanced/           # Design Hit Counter, Task Scheduler
```

Run any file directly to see it work, e.g.:

```bash
python 02_deque/sliding_window_maximum.py
```
