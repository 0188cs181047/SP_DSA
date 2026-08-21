"""
Rotting Oranges - Multi-source BFS on a Grid   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
You are given an `m x n` grid where each cell is one of:
0 (empty), 1 (fresh orange), or 2 (rotten orange). Every minute, any fresh
orange that is 4-directionally adjacent to a rotten orange also becomes
rotten. Return the minimum number of minutes until no cell has a fresh
orange, or -1 if that is impossible.

Example:
    Input:  grid = [[2, 1, 1],
                     [1, 1, 0],
                     [0, 1, 1]]
    Output: 4

    minute 0:        minute 1:        minute 2:
    [2, 1, 1]        [2, 2, 1]        [2, 2, 2]
    [1, 1, 0]        [2, 1, 0]        [2, 2, 0]
    [0, 1, 1]        [0, 1, 1]        [0, 2, 1]

    minute 3:        minute 4:
    [2, 2, 2]        [2, 2, 2]
    [2, 2, 0]        [2, 2, 0]
    [0, 2, 2]        [0, 2, 2]   <- last fresh orange rotted here

Approach:
- Treat every rotten orange as a BFS source simultaneously - push all of
  them into the queue up front instead of running BFS once per orange.
  This "multi-source" trick makes the rot spread outward in true minute-
  by-minute waves, since BFS naturally explores level by level.
- Process the queue one full level (one minute) at a time: pop everything
  currently queued, rot each fresh 4-directional neighbor exactly once,
  and push those newly-rotten cells for the next level. Track the minute
  count only when a level actually rotted something.
- Keep a running count of fresh oranges; every time a cell rots, decrement
  it. If that count hits 0, all oranges rotted.
- Edge cases: a grid with no fresh oranges at all rots in 0 minutes; a
  grid where some fresh orange is unreachable (isolated by 0s or out of
  range of any rotten orange) means the count never reaches 0, so return
  -1 once the BFS drains with fresh oranges still remaining.

Time Complexity:  O(rows * cols) - every cell is enqueued and processed once
Space Complexity: O(rows * cols) - the queue holds up to all cells at once
"""

from collections import deque


def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    minutes = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        rotted_this_minute = False

        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))
                    rotted_this_minute = True

        if rotted_this_minute:
            minutes += 1

    return minutes if fresh_count == 0 else -1


if __name__ == "__main__":
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    print("grid:")
    for row in grid:
        print(" ", row)
    print("minutes until all oranges rot:", oranges_rotting(grid))
    # 4
