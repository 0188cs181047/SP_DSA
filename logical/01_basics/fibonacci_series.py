"""
Print the First N Fibonacci Numbers - Iterative Sequence Building   (Difficulty: Easy)
Asked at: TCS, Infosys, Adobe

Problem:
Given an integer n, generate the first n numbers of the Fibonacci sequence,
where each number is the sum of the two preceding ones, starting with 0, 1.

Example:
    Input: n = 8
    Output: [0, 1, 1, 2, 3, 5, 8, 13]

Approach:
- Build the sequence iteratively, keeping only the last two values needed
  to compute the next one, rather than recomputing from scratch each time.
- This runs in O(n) time and O(1) extra working space (besides the output
  list itself, which necessarily holds n values).
- Edge cases: n = 0 returns an empty list, n = 1 returns just [0].
- Note: if the task only needs the single Nth Fibonacci number (not the
  whole series), that's better solved with DP/memoization to avoid
  recomputation - see the dynamic_programming module for that version.

Time Complexity:  O(n)
Space Complexity: O(1) extra space, O(n) for the output list
"""


def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    n = 8
    output = fibonacci_series(n)
    print("n =", n)
    print("Output:", output)
