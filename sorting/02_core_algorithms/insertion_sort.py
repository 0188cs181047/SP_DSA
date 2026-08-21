"""
Insertion Sort - Build a Sorted Prefix   (Difficulty: Easy)
Asked at: TCS, Infosys, Amazon

Problem:
Given an array of integers, sort it in ascending order using insertion
sort: grow a sorted prefix at the front of the array one element at a
time, inserting each new element into its correct position within that
prefix.

Example:
    Input:  [5, 2, 4, 6, 1, 3]
    Output: [1, 2, 3, 4, 5, 6]

Approach:
- Treat arr[0] as a sorted prefix of length 1. For each next element
  (the "key"), shift every element in the sorted prefix that is greater
  than the key one slot to the right, opening up a gap for it.
- Drop the key into the gap once you hit an element <= key (or the start
  of the array) - this keeps the prefix sorted after every step, which is
  the loop invariant.
- Edge cases: empty/single-element array (loop never runs, already
  "sorted"). Performance shines on nearly-sorted input - each key only
  shifts past a handful of elements, giving close to O(n) instead of the
  O(n^2) worst case on reverse-sorted input.

Time Complexity:  O(n^2) worst/average case, O(n) best case (nearly sorted)
Space Complexity: O(1) extra space (sorts in place)
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    nums = [5, 2, 4, 6, 1, 3]
    print("Before:", nums)
    insertion_sort(nums)
    print("After: ", nums)
