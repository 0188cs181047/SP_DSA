# Stack

A **Stack** is a linear data structure that follows **LIFO (Last In, First Out)** order — the last element added is the first one removed. Think of a stack of plates: you add and remove from the top only.

```
push(4) ->  |  4  |  <- top
            |  3  |
            |  2  |
            |  1  |
            -------
```

## Core Operations

| Operation | Description | Time Complexity |
|---|---|---|
| `push(x)` | Add element `x` to the top | O(1) |
| `pop()` | Remove and return the top element | O(1) |
| `peek()` / `top()` | Look at the top element without removing it | O(1) |
| `is_empty()` | Check if the stack has no elements | O(1) |

All operations happen at one end (the "top"), which is what makes them O(1) — no shifting required.

## Implementations

- **Array-based**: use a dynamic array, `push`/`pop` from the end. Simple and cache-friendly.
- **Linked-list-based**: `push`/`pop` from the head. No resizing cost, but extra pointer memory per node.

## When to Use a Stack

- You need to reverse order (last-added, first-processed).
- Matching/undo problems: parentheses matching, undo/redo in editors, browser back button.
- Tracking nested/recursive state: function call stack, DFS traversal (explicit stack instead of recursion).
- Backtracking algorithms.

## Common Problems Solved with Stacks

- Valid Parentheses / balanced brackets
- Evaluate postfix/prefix expressions
- Next Greater Element (monotonic stack)
- Min Stack (get minimum in O(1))
- Implementing DFS iteratively
- Undo functionality in applications
