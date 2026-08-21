"""
Quick Sort - Divide & Conquer + Partition   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
Given an array of integers, sort it in ascending order using the quicksort
algorithm. Do it in place - partition the array around a pivot so that
everything smaller ends up on its left and everything bigger ends up on
its right, then recursively sort each side.

Example:
    Input:  [8, 3, 1, 7, 0, 10, 2]
    Output: [0, 1, 2, 3, 7, 8, 10]

Approach:
- Pick a pivot from the current subarray, then partition (Lomuto scheme):
  walk the subarray and swap elements <= pivot into a growing "smaller"
  region on the left, finally dropping the pivot right after that region.
- Recurse independently on the left partition (before the pivot) and the
  right partition (after the pivot) - the pivot itself is already in its
  final sorted position and never needs to be touched again.
- Edge cases: empty/single-element arrays (recursion just bottoms out),
  and duplicate values (handled fine by the <= comparison in partition).
  A naive "always pick the last element as pivot" degrades to O(n^2) on
  already-sorted or reverse-sorted input, since every partition is maximally
  unbalanced; picking a random pivot (as done below) avoids that worst case
  for any fixed input pattern.

Time Complexity:  O(n log n) average, O(n^2) worst case (bad pivot choices)
Space Complexity: O(log n) average recursion depth, O(n) worst case
"""

import random


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr, low, high):
    if low < high:
        pivot_index = _partition(arr, low, high)
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)


def _partition(arr, low, high):
    # randomize the pivot so already-sorted/reverse-sorted input can't
    # force the O(n^2) worst case
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    nums = [8, 3, 1, 7, 0, 10, 2]
    print("Before:", nums)
    quick_sort(nums)
    print("After: ", nums)
