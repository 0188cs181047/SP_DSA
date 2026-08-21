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

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_basics](01_basics) | Climbing Stairs / Fibonacci | [climbing_stairs.py](01_basics/climbing_stairs.py) | 1D DP | Easy | Amazon, Adobe, Microsoft, TCS |
| 2 | [01_basics](01_basics) | House Robber | [house_robber.py](01_basics/house_robber.py) | 1D DP (include/exclude) | Easy/Medium | Amazon, Google, Meta |
| 3 | [02_1d_dp](02_1d_dp) | Coin Change (Minimum Coins) | [coin_change.py](02_1d_dp/coin_change.py) | Unbounded Knapsack | Medium | Amazon, Google, Uber |
| 4 | [02_1d_dp](02_1d_dp) | Longest Increasing Subsequence | [longest_increasing_subsequence.py](02_1d_dp/longest_increasing_subsequence.py) | 1D DP / Binary Search | Medium | Amazon, Google, Microsoft |
| 5 | [../array/05_kadane](../array/05_kadane) | Maximum Subarray Sum (Kadane's) | [kadanes_algorithm.py](../array/05_kadane/kadanes_algorithm.py) | DP / Greedy | Medium | Amazon, Microsoft, LinkedIn |
| 6 | [03_2d_dp_strings](03_2d_dp_strings) | Longest Common Subsequence (LCS) | [longest_common_subsequence.py](03_2d_dp_strings/longest_common_subsequence.py) | 2D DP | Medium | Amazon, Google, Microsoft |
| 7 | [03_2d_dp_strings](03_2d_dp_strings) | Edit Distance | [edit_distance.py](03_2d_dp_strings/edit_distance.py) | 2D DP | Hard | Google, Amazon, Microsoft |
| 8 | [03_2d_dp_strings](03_2d_dp_strings) | Longest Palindromic Substring | [longest_palindromic_substring.py](03_2d_dp_strings/longest_palindromic_substring.py) | Expand Around Center | Medium | Amazon, Microsoft, Meta |
| 9 | [04_knapsack_family](04_knapsack_family) | 0/1 Knapsack | [knapsack_01.py](04_knapsack_family/knapsack_01.py) | 2D DP | Medium | Amazon, Google |
| 10 | [04_knapsack_family](04_knapsack_family) | Subset Sum | [subset_sum.py](04_knapsack_family/subset_sum.py) | Boolean 2D DP | Medium | Amazon, Microsoft |
| 11 | [04_knapsack_family](04_knapsack_family) | Partition Equal Subset Sum | [partition_equal_subset_sum.py](04_knapsack_family/partition_equal_subset_sum.py) | Subset Sum Variant | Medium | Amazon, Google, Meta |
| 12 | [05_grid_dp](05_grid_dp) | Unique Paths in a Grid | [unique_paths.py](05_grid_dp/unique_paths.py) | 2D Grid DP | Medium | Amazon, Google, Microsoft |
| 13 | [05_grid_dp](05_grid_dp) | Minimum Path Sum in a Grid | [minimum_path_sum.py](05_grid_dp/minimum_path_sum.py) | 2D Grid DP | Medium | Amazon, Microsoft |
| 14 | [06_advanced](06_advanced) | Word Break | [word_break.py](06_advanced/word_break.py) | 1D DP + HashSet | Medium | Amazon, Google, Meta |
| 15 | [06_advanced](06_advanced) | Best Time to Buy/Sell Stock with Cooldown/Fee | [stock_dp_state_machine.py](06_advanced/stock_dp_state_machine.py) | DP State Machine | Hard | Amazon, Google |

## How to Pick the Right Pattern in an Interview

- One sequence, decision at each index depends on a few previous states? → **1D DP**
- Two strings/sequences being compared or aligned? → **2D DP table**
- Items with a weight/capacity constraint, choosing a subset? → **Knapsack family**
- Moving through a grid with limited directions? → **2D grid DP**
- "Can we reach/build/partition an exact target value?" → **Boolean subset-style DP**
- Repeated decisions with multiple "modes" (holding / not holding / cooldown)? → **DP state machine**

## Folder Structure

```
dynamic_programming/
├── README.md
├── 01_basics/            # Climbing Stairs, House Robber
├── 02_1d_dp/             # Coin Change, Longest Increasing Subsequence
├── 03_2d_dp_strings/     # LCS, Edit Distance, Longest Palindromic Substring
├── 04_knapsack_family/   # 0/1 Knapsack, Subset Sum, Partition Equal Subset Sum
├── 05_grid_dp/           # Unique Paths, Minimum Path Sum
└── 06_advanced/          # Word Break, Stock DP State Machine

(Maximum Subarray / Kadane's Algorithm lives in ../array/05_kadane/ — it's DP in disguise)
```

Run any file directly to see it work, e.g.:

```bash
python 03_2d_dp_strings/edit_distance.py
```
