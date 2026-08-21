"""
Climbing Stairs / Fibonacci - 1D DP   (Difficulty: Easy)
Asked at: Amazon, Adobe, Microsoft, TCS

Problem:
You are climbing a staircase that takes n steps to reach the top. Each time
you can either climb 1 step or 2 steps. Count the number of distinct ways
you can climb to the top.

Example:
    Input: n = 5
    Output: 8

Approach:
- Let dp[i] be the number of distinct ways to reach step i. To land on step
  i you either took a single step from step i-1, or a double step from step
  i-2, so dp[i] = dp[i-1] + dp[i-2] - exactly the Fibonacci recurrence.
- The naive recursive solution recomputes the same subproblems an
  exponential number of times; memoizing it collapses that to O(n) distinct
  calls. Since only the last two values are ever needed, an iterative
  bottom-up pass drops the space from O(n) to O(1).
- Base cases: dp[0] = 1 (one way to "stay put" at the bottom) and
  dp[1] = 1 (only one way to take a single step).

Time Complexity:  O(n) for the memoized and bottom-up versions (O(2^n) for the naive recursion)
Space Complexity: O(n) for the memoized version (call stack + cache), O(1) for the bottom-up version
"""


def climb_stairs_naive(n):
    # Plain exponential recursion - shown for contrast, do not use for large n.
    if n <= 1:
        return 1
    return climb_stairs_naive(n - 1) + climb_stairs_naive(n - 2)


def climb_stairs_memo(n, cache=None):
    # Top-down recursion with memoization - O(n) calls instead of O(2^n).
    if cache is None:
        cache = {}
    if n <= 1:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = climb_stairs_memo(n - 1, cache) + climb_stairs_memo(n - 2, cache)
    return cache[n]


def climb_stairs(n):
    # Bottom-up, O(1) space: only the previous two values are ever needed.
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1  # ways to reach step 0 and step 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


if __name__ == "__main__":
    n = 5
    print(f"Naive recursion: climb_stairs_naive({n}) = {climb_stairs_naive(n)}")
    print(f"Memoized:        climb_stairs_memo({n}) = {climb_stairs_memo(n)}")
    print(f"Bottom-up O(1):  climb_stairs({n}) = {climb_stairs(n)}")
