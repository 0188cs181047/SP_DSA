"""
Unique Paths in a Grid - 2D Grid DP   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
A robot starts at the top-left corner of an m x n grid and wants to reach
the bottom-right corner. At every step the robot can only move either down
or right. Count how many distinct paths exist from the start to the finish.

Example:
    Input: m = 3, n = 7
    Output: 28

Approach:
- dp[r][c] = number of distinct ways to reach cell (r, c) from the top-left.
- A cell can only be entered from directly above or directly from the left,
  so dp[r][c] = dp[r-1][c] + dp[r][c-1].
- Base case: the entire first row and the entire first column are all 1,
  since there is only one way to reach any of those cells (a single
  straight line of moves).
- Edge cases: if m == 1 or n == 1, the answer is always 1 (a single row or
  column has exactly one path).

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""


def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    m, n = 3, 7
    print(unique_paths(m, n))  # 28
