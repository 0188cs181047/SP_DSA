"""
Flood Fill   (Difficulty: Easy)
Asked at: Google, Amazon

Problem:
Given an image (2D grid of colors), a starting pixel (sr, sc), and a new
color, replace the color of the starting pixel and every pixel connected
to it (4-directionally) that has the *same original color* with the new
color. This is exactly the "paint bucket" tool in image editors — and
exactly the same pattern as Number of Islands.

Example:
    image = [[1,1,1],
              [1,1,0],
              [1,0,1]]
    sr, sc, newColor = 1, 1, 2

Flow diagram (cells that get repainted are marked *):
    1 1 1        [2*] [2*] [2*]
    1 1 0   -->   [2*] [2*]  0
    1 0 1         [2*]  0    1

    Result: [[2,2,2],[2,2,0],[2,0,1]]

Approach:
- Remember the original color at (sr, sc).
- DFS/BFS from (sr, sc); repaint any neighboring cell that still has the
  original color. Stop at cells with a different color (boundary).
- Guard against the case newColor == original color (would infinite loop).

Time Complexity:  O(rows * cols)
Space Complexity: O(rows * cols) for the recursion stack in the worst case.
"""

def flood_fill(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or image[r][c] != original_color):
            return
        image[r][c] = new_color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]

    result = flood_fill(image, 1, 1, 2)
    for row in result:
        print(row)
