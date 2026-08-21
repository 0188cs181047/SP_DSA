# Linked List

A **Linked List** is a linear data structure where elements (**nodes**) are stored anywhere in memory, and each node points to the next one. Unlike an array, elements aren't contiguous — order is maintained through pointers, not memory position.

```
[10 | next] -> [20 | next] -> [30 | next] -> [40 | None]
   head
```

Each node typically has two parts:
```
data  : the value stored
next  : a pointer/reference to the next node (None if it's the last node)
```

## Types

| Type | Description |
|---|---|
| Singly Linked List | Each node points only to the `next` node |
| Doubly Linked List | Each node points to both `next` and `prev`, allowing backward traversal |
| Circular Linked List | The last node points back to the head instead of `None`, forming a loop |

## Operations & Time Complexity

| Operation | Time Complexity | Notes |
|---|---|---|
| Access by index | O(n) | Must traverse from head |
| Search | O(n) | No random access |
| Insert at head | O(1) | Just repoint the head |
| Insert at tail | O(n) singly / O(1) doubly with tail pointer | |
| Insert at middle | O(n) to find position, O(1) to link | |
| Delete at head | O(1) | |
| Delete at middle/tail | O(n) to find, O(1) to unlink | |

## Arrays vs Linked Lists

| | Array | Linked List |
|---|---|---|
| Memory layout | Contiguous | Scattered, linked via pointers |
| Access by index | O(1) | O(n) |
| Insert/Delete at start | O(n) | O(1) |
| Extra memory per element | None | Pointer(s) overhead |
| Cache performance | Good | Poor (nodes scattered in memory) |

## When to Use Linked Lists

- Frequent insertions/deletions at the **beginning** or in the **middle**, without shifting elements.
- You don't need random access by index.
- Implementing other structures: stacks, queues, and hash table chaining are commonly built on linked lists.

## Common Problems Solved with Linked Lists

- Reverse a linked list (iterative and recursive)
- Detect a cycle (Floyd's Tortoise and Hare / slow-fast pointers)
- Find the middle node in one pass
- Merge two sorted linked lists
- Remove the Nth node from the end

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [single](single) | Insert a Node at the Beginning | [insert_at_beginning.py](single/insert_at_beginning.py) | Singly LL Basics | Easy | TCS, Infosys, Amazon |
| 2 | [single](single) | Insert a Node at the End | [insert_at_end.py](single/insert_at_end.py) | Singly LL Basics | Easy | TCS, Wipro, Amazon |
| 3 | [02_reversal](02_reversal) | Reverse a Linked List (Iterative & Recursive) | [reverse_linked_list.py](02_reversal/reverse_linked_list.py) | In-place Pointer Reversal | Easy/Medium | Amazon, Microsoft, Google, TCS |
| 4 | [02_reversal](02_reversal) | Find the Middle Node | [find_middle_node.py](02_reversal/find_middle_node.py) | Slow/Fast Pointers | Easy | Amazon, Microsoft |
| 5 | [03_cycle_detection](03_cycle_detection) | Detect a Cycle (Floyd's Algorithm) | [detect_cycle.py](03_cycle_detection/detect_cycle.py) | Slow/Fast Pointers | Medium | Amazon, Microsoft, Google |
| 6 | [03_cycle_detection](03_cycle_detection) | Find the Start of a Cycle | [cycle_start_node.py](03_cycle_detection/cycle_start_node.py) | Floyd's, Phase 2 | Medium | Amazon, Adobe |
| 7 | [04_merge_manipulate](04_merge_manipulate) | Merge Two Sorted Linked Lists | [merge_two_sorted_lists.py](04_merge_manipulate/merge_two_sorted_lists.py) | Two-pointer Merge | Easy | Amazon, Microsoft, Apple |
| 8 | [04_merge_manipulate](04_merge_manipulate) | Remove the Nth Node From the End | [remove_nth_from_end.py](04_merge_manipulate/remove_nth_from_end.py) | Fast/Slow + Offset | Medium | Amazon, Meta |
| 9 | [04_merge_manipulate](04_merge_manipulate) | Add Two Numbers (as linked lists) | [add_two_numbers.py](04_merge_manipulate/add_two_numbers.py) | Simulated Addition + Carry | Medium | Amazon, Microsoft, Bloomberg |
| 10 | [05_advanced](05_advanced) | Palindrome Linked List | [palindrome_linked_list.py](05_advanced/palindrome_linked_list.py) | Fast/Slow + Reverse Half | Easy/Medium | Amazon, Meta |
| 11 | [05_advanced](05_advanced) | Copy a List with Random Pointer | [copy_list_with_random_pointer.py](05_advanced/copy_list_with_random_pointer.py) | HashMap Cloning | Medium/Hard | Amazon, Google, Meta |
| 12 | [05_advanced](05_advanced) | Merge K Sorted Lists | [merge_k_sorted_lists.py](05_advanced/merge_k_sorted_lists.py) | Min-Heap | Hard | Amazon, Google, Microsoft |
| 13 | [05_advanced](05_advanced) | Design an LRU Cache | [lru_cache.py](05_advanced/lru_cache.py) | Doubly Linked List + HashMap | Medium/Hard | Amazon, Google, Meta, Uber |

## How to Pick the Right Pattern in an Interview

- Need to reverse the whole list or a part of it? → **Iterative/recursive pointer reversal**
- Need the middle node, cycle detection, or "Nth from the end"? → **Slow/Fast (two-speed) pointers**
- Need to merge sorted lists? → **Two-pointer merge** (2 lists) or a **min-heap** (K lists)
- Need O(1) get/put with least-recently-used eviction? → **Doubly Linked List + HashMap** (LRU Cache)
- Need to clone a list that has extra pointers (e.g. random)? → **HashMap: old node → new node**

## Folder Structure

```
linked_list/
├── README.md
├── single/                  # Insert at Beginning / End (basics)
├── 02_reversal/              # Reverse List, Find Middle Node
├── 03_cycle_detection/       # Detect Cycle, Find Cycle Start
├── 04_merge_manipulate/      # Merge Two Sorted Lists, Remove Nth From End, Add Two Numbers
└── 05_advanced/               # Palindrome Check, Copy Random Pointer List, Merge K Lists, LRU Cache
```

Run any file directly to see it work, e.g.:

```bash
python 05_advanced/lru_cache.py
```
