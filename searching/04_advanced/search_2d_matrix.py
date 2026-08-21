"""
Search in a Sorted 2D Matrix - Binary Search (flattened) or Staircase Search   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Google

Problem:
Given an m x n matrix and a target value, determine whether the target
exists in the matrix. Two flavors of "sorted matrix" show up in
interviews: (1) each row is sorted left-to-right AND the first element
of every row is greater than the last element of the previous row, so
the whole grid is really a sorted 1D array reshaped into rows, or
(2) each row is sorted left-to-right and each column is sorted
top-to-bottom independently, with no guarantee between rows (a row can
overlap the value range of the row above or below it).

Example:
    Input:  matrix = [[1,  3,  5,  7],
                       [10, 11, 16, 20],
                       [23, 30, 34, 60]]
            target = 3
    Output: True   (flattened case: 1,3,5,7,10,11,... is one sorted list)

    Input:  matrix = [[1,  4,  7, 11, 15],
                       [2,  5,  8, 12, 19],
                       [3,  6,  9, 16, 22],
                       [10, 13, 14, 17, 24],
                       [18, 21, 23, 26, 30]]
            target = 5
    Output: True   (row/column sorted, but rows overlap - not flattenable)

    staircase search from the top-right corner:
    [ 1  4  7 11 15]   start at (0,4) = 15, 15 > 5  -> move left
    [ 2  5  8 12 19]   (0,3) = 11, 11 > 5  -> move left
    [ 3  6  9 16 22]   (0,2) =  7,  7 > 5  -> move left
    [10 13 14 17 24]   (0,1) =  4,  4 < 5  -> move down
    [18 21 23 26 30]   (1,1) =  5  -> found

Approach:
- Flattened case: index k of a conceptually flattened row-major array
  maps back to matrix[k // cols][k % cols], so run a plain binary
  search over k in [0, rows*cols - 1] without ever materializing the
  flattened array.
- Staircase case: start at the top-right corner. If the current value
  equals the target, done. If it's bigger, the whole column below it is
  also too big (columns sort top-to-bottom), so drop that column. If
  it's smaller, the whole row to the left is too small (rows sort
  left-to-right), so drop that row. Each step eliminates a full row or
  column, so the walk finishes in at most rows + cols steps.
- The staircase approach also happens to work on the fully-flattened
  matrix from case 1, but binary search is asymptotically faster there,
  so pick the technique based on which sortedness guarantee actually
  holds for the input.
- Edge cases: an empty matrix, or a matrix whose rows are empty, should
  just return False instead of raising an index error.

Time Complexity:  O(log(rows * cols)) for the flattened case;
                   O(rows + cols) for the staircase case
Space Complexity: O(1) for both
"""


def search_matrix_flattened(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        value = matrix[mid // cols][mid % cols]

        if value == target:
            return True
        elif value < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


def search_matrix_staircase(matrix, target):
    if not matrix or not matrix[0]:
        return False

    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        value = matrix[row][col]

        if value == target:
            return True
        elif value > target:
            col -= 1
        else:
            row += 1

    return False


if __name__ == "__main__":
    flattened_matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]
    print(search_matrix_flattened(flattened_matrix, 3))   # True
    print(search_matrix_flattened(flattened_matrix, 13))  # False

    staircase_matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(search_matrix_staircase(staircase_matrix, 5))   # True
    print(search_matrix_staircase(staircase_matrix, 20))  # False
