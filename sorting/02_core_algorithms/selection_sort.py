"""
Selection Sort - Repeated Minimum Selection   (Difficulty: Easy)
Asked at: TCS, Infosys, Wipro

Problem:
Given an array of integers, sort it in ascending order using selection
sort: repeatedly find the minimum element in the remaining unsorted
portion and swap it into place at the front of that portion.

Example:
    Input:  [64, 25, 12, 22, 11]
    Output: [11, 12, 22, 25, 64]

Approach:
- Split the array into a sorted prefix (initially empty) and an unsorted
  suffix (initially the whole array).
- For each position i from left to right, scan the unsorted suffix to
  find the index of its minimum element, then swap that minimum into
  position i - this grows the sorted prefix by one each pass.
- Edge cases: empty/single-element array (loop never runs, already
  "sorted"). Unlike bubble/insertion sort, selection sort does the same
  O(n^2) comparisons regardless of input order (no early exit on
  already-sorted data), but it makes at most O(n) swaps - useful when
  writes are expensive (e.g. flash memory).

Time Complexity:  O(n^2) best, average, and worst case
Space Complexity: O(1) extra space (sorts in place)
"""


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    nums = [64, 25, 12, 22, 11]
    print("Before:", nums)
    selection_sort(nums)
    print("After: ", nums)
