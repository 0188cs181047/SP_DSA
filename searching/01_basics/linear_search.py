"""
Linear Search - Sequential Scan   (Difficulty: Easy)
Asked at: TCS, Infosys, Wipro, Amazon

Problem:
Given an array of integers and a target value, find the index of the target
in the array. The array is not necessarily sorted. If the target does not
appear in the array, return -1.

Example:
    Input: arr = [5, 3, 8, 1, 9, 2], target = 9
    Output: 4

Approach:
- Walk the array from left to right, comparing each element to the target.
- Return the index the moment a match is found - no need to look further.
- Works on unsorted data because it makes no assumption about ordering,
  unlike binary search which requires a sorted array.
- Edge cases: empty array (nothing to find, return -1) and a target that
  appears multiple times (this returns the first occurrence).

Time Complexity:  O(n) - in the worst case every element is checked once
Space Complexity: O(1) - no extra memory is used beyond the loop index
"""


def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1


if __name__ == "__main__":
    nums = [5, 3, 8, 1, 9, 2]
    target = 9
    result = linear_search(nums, target)
    print("Array:", nums)
    print("Target:", target)
    print("Index found at:", result)

    missing_target = 100
    print("Searching for missing value", missing_target, "->", linear_search(nums, missing_target))
