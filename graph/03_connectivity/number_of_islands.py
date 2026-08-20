"""
Number of Islands   (Difficulty: Medium)
Asked at: Amazon, Google, Meta, Microsoft — one of the most repeated grid+graph questions

Problem:
Given an m x n grid of '1' (land) and '0' (water), count the number of
islands. An island is surrounded by water and formed by connecting
adjacent lands horizontally or vertically (a grid is just a graph in
disguise — each cell is a node, adjacent cells are edges).

Example grid:
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1

Flow diagram (islands circled):
    [1 1] 0  0  0        Island #1: top-left 2x2 block
    [1 1] 0  0  0
     0  0 [1] 0  0       Island #2: single cell
     0  0  0 [1 1]       Island #3: bottom-right pair

    Answer: 3

Approach:
- Scan every cell. When you find an unvisited '1', that's a brand-new
  island — increment the count and DFS/BFS to sink (mark visited) every
  connected '1' so it isn't counted again.
- This is DFS/BFS on an implicit graph where nodes are (row, col) grid
  cells instead of explicit vertex objects.

Time Complexity:  O(rows * cols) — each cell visited once.
Space Complexity: O(rows * cols) worst case for the recursion/BFS queue.
"""

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] == "0" or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands


if __name__ == "__main__":
    grid = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]

    print("Number of islands:", num_islands(grid))
