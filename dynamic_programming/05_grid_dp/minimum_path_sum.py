"""
Minimum Path Sum in a Grid - 2D Grid DP   (Difficulty: Medium)
Asked at: Amazon, Microsoft

Problem:
Given an m x n grid filled with non-negative numbers, find a path from the
top-left cell to the bottom-right cell that minimizes the sum of the
numbers along the path. You may only move either down or right at each
step.

Example:
    Input: grid = [[1, 3, 1],
                    [1, 5, 1],
                    [4, 2, 1]]
    Output: 7   (path 1 -> 3 -> 1 -> 1 -> 1)

Approach:
- dp[r][c] = the minimum cost to reach cell (r, c) from the top-left.
- A cell can only be entered from directly above or directly from the
  left, so dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]).
- Base case: the first row can only be entered by moving right, so
  dp[0][c] = grid[0][c] + dp[0][c-1]; the first column can only be
  entered by moving down, so dp[r][0] = grid[r][0] + dp[r-1][0].
- Edge cases: a 1x1 grid has a path sum equal to its single cell's value.

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""


def minimum_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0:
                dp[r][c] = grid[r][c]
            elif r == 0:
                dp[r][c] = grid[r][c] + dp[r][c - 1]
            elif c == 0:
                dp[r][c] = grid[r][c] + dp[r - 1][c]
            else:
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]
    print(minimum_path_sum(grid))  # 7
