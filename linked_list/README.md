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
