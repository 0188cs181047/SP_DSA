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

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_basics](01_basics) | Implement a Stack (array & linked-list based) | [implement_stack.py](01_basics/implement_stack.py) | Core Data Structure | Easy | TCS, Infosys, Amazon |
| 2 | [01_basics](01_basics) | Valid Parentheses | [valid_parentheses.py](01_basics/valid_parentheses.py) | Stack Matching | Easy | Amazon, Google, Microsoft, Bloomberg |
| 3 | [02_monotonic_stack](02_monotonic_stack) | Next Greater Element | [next_greater_element.py](02_monotonic_stack/next_greater_element.py) | Monotonic Stack | Medium | Amazon, Microsoft, Bloomberg |
| 4 | [02_monotonic_stack](02_monotonic_stack) | Daily Temperatures | [daily_temperatures.py](02_monotonic_stack/daily_temperatures.py) | Monotonic Stack | Medium | Amazon, Google |
| 5 | [02_monotonic_stack](02_monotonic_stack) | Largest Rectangle in Histogram | [largest_rectangle_histogram.py](02_monotonic_stack/largest_rectangle_histogram.py) | Monotonic Stack | Hard | Google, Amazon, Uber |
| 6 | [03_expression_evaluation](03_expression_evaluation) | Evaluate Reverse Polish Notation | [evaluate_rpn.py](03_expression_evaluation/evaluate_rpn.py) | Stack Evaluation | Medium | Amazon, LinkedIn, Google |
| 7 | [03_expression_evaluation](03_expression_evaluation) | Basic Calculator (+, -, parentheses) | [basic_calculator.py](03_expression_evaluation/basic_calculator.py) | Stack for Sign Context | Hard | Google, Amazon, Microsoft |
| 8 | [04_advanced](04_advanced) | Design a Min Stack (O(1) getMin) | [min_stack.py](04_advanced/min_stack.py) | Auxiliary Stack | Medium | Amazon, Google, Meta |
| 9 | [04_advanced](04_advanced) | Implement a Queue Using Two Stacks | [queue_using_stacks.py](04_advanced/queue_using_stacks.py) | Two Stacks | Easy/Medium | Amazon, Microsoft |
| 10 | [04_advanced](04_advanced) | Decode String (e.g. "3[a2[c]]") | [decode_string.py](04_advanced/decode_string.py) | Stack of (count, string) | Medium | Google, Amazon, Meta |

## How to Pick the Right Pattern in an Interview

- Need to match/validate nested pairs (brackets, tags)? → **Stack matching**
- Need "next greater/smaller" or "how far until X" for every element? → **Monotonic stack**
- Need to evaluate an expression with operators/parentheses? → **Stack-based evaluation**
- Need O(1) access to a running min/max alongside push/pop? → **Auxiliary stack**
- Need to simulate FIFO order using only stacks, or decode a nested/repeated structure? → **Two stacks / stack of (count, partial-result)**

## Folder Structure

```
stack/
├── README.md
├── 01_basics/                 # Implement Stack, Valid Parentheses
├── 02_monotonic_stack/        # Next Greater Element, Daily Temperatures, Largest Rectangle in Histogram
├── 03_expression_evaluation/  # Evaluate RPN, Basic Calculator
└── 04_advanced/               # Min Stack, Queue Using Stacks, Decode String
```

Run any file directly to see it work, e.g.:

```bash
python 02_monotonic_stack/largest_rectangle_histogram.py
```
