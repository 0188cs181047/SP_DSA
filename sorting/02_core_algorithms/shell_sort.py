"""
Shell Sort - Gapped Insertion Sort   (Difficulty: Medium)
Asked at: Amazon, Microsoft

Problem:
Given an array of integers, sort it in ascending order using shell sort:
an extension of insertion sort that first compares and moves elements
far apart, then progressively shrinks the gap down to 1.

Example:
    Input:  [12, 34, 54, 2, 3]
    Output: [2, 3, 12, 34, 54]

Approach:
- Start with a large gap (n // 2) and run an insertion sort where
  elements gap positions apart are compared/shifted instead of adjacent
  ones - this moves far-out-of-place elements toward their final spot
  quickly instead of one step at a time.
- Halve the gap each round and repeat, finishing with gap = 1, which is
  a plain insertion sort - but by then the array is "mostly sorted", so
  that final pass is cheap.
- Edge cases: empty/single-element array (loop never runs). The exact
  time complexity depends heavily on the gap sequence chosen; the
  classic Shell (n/2, n/4, ..., 1) sequence used below gives O(n^2)
  worst case but performs much better than plain insertion sort in
  practice.

Time Complexity:  O(n^2) worst case (Shell's gap sequence), O(n log n) best case
Space Complexity: O(1) extra space (sorts in place)
"""


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2

    return arr


if __name__ == "__main__":
    nums = [12, 34, 54, 2, 3]
    print("Before:", nums)
    shell_sort(nums)
    print("After: ", nums)
