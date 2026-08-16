# Dynamic Programming (DP)

**Dynamic Programming** is a technique for solving problems by breaking them into overlapping subproblems, solving each subproblem once, and reusing the result instead of recomputing it.

It applies when a problem has:

1. **Optimal Substructure** — the optimal solution can be built from optimal solutions to its subproblems.
2. **Overlapping Subproblems** — the same subproblems are solved repeatedly in a naive (e.g. recursive) approach.

## Example: Fibonacci

Naive recursion recomputes the same values many times:

```
fib(5)
├── fib(4)
│   ├── fib(3)          <- computed here...
│   │   ├── fib(2)
│   │   └── fib(1)
│   └── fib(2)
└── fib(3)               <- ...and recomputed here again
    ├── fib(2)
    └── fib(1)
```

Naive recursive `fib(n)` is O(2^n). With DP, each value is computed once: O(n).

## Two Approaches

| Approach | Description | Direction |
|---|---|---|
| **Memoization** (Top-Down) | Recursion + cache: store each subproblem's result the first time it's computed, return the cached value next time | Top-down (start from the original problem) |
| **Tabulation** (Bottom-Up) | Build a table iteratively, starting from the smallest subproblems up to the final answer | Bottom-up (start from the base cases) |

```python
# Memoization (Top-Down)
def fib(n, cache={}):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]

# Tabulation (Bottom-Up)
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

## Complexity

| | Naive Recursion | DP (Memo or Tabulation) |
|---|---|---|
| Fibonacci(n) | O(2^n) time | O(n) time, O(n) space |

Space can often be optimized further — e.g. Fibonacci only needs the last two values, so it can run in O(1) space instead of O(n).

## When to Use DP

- The problem asks for an **optimal value** (min/max/count of ways) and naive recursion visibly recomputes the same subproblems.
- Look for phrases like "minimum cost to...", "number of ways to...", "longest/shortest...".

## Common Problems Solved with DP

- Fibonacci / Climbing Stairs
- 0/1 Knapsack
- Longest Common Subsequence (LCS)
- Longest Increasing Subsequence (LIS)
- Coin Change (minimum coins / number of ways)
- Edit Distance
- House Robber
