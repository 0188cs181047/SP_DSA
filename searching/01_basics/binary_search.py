"""
Binary Search (Iterative & Recursive) - Divide and Conquer   (Difficulty: Easy)
Asked at: Amazon, Google, Microsoft

Problem:
Given a sorted array of integers and a target value, find the index of the
target in the array. If the target does not appear in the array, return -1.
Solve it using both an iterative loop and a recursive helper.

Example:
    Input: arr = [1, 3, 5, 7, 9, 11, 13], target = 7
    Output: 3

    low                mid               high
     |                  |                 |
    [1, 3, 5, 7, 9, 11, 13]
     compare target(7) to arr[mid]=7 -> match, return index

Approach:
- Keep a low/high window over the sorted array and repeatedly look at the
  middle element.
- If the middle element equals the target, done. If the target is smaller,
  the answer (if any) must be in the left half, so drop the right half by
  moving high to mid - 1. If the target is larger, drop the left half by
  moving low to mid + 1.
- Each comparison halves the search space, which is what gives the
  logarithmic running time.
- The recursive version does the exact same narrowing, just expressed as a
  function call on the shrinking [low, high] range instead of a while loop.
- Edge cases: empty array (low > high immediately, return -1), target smaller
  than every element or larger than every element (loop/recursion still
  terminates correctly and returns -1), and duplicate values (either matching
  index can be returned since there is no requirement to find the first one).

Time Complexity:  O(log n) - the search window is halved on every step
Space Complexity: O(1) for the iterative version, O(log n) for the recursive
                   version due to the call stack
"""


def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]
    target = 7

    print("Array:", nums)
    print("Target:", target)
    print("Iterative result:", binary_search_iterative(nums, target))
    print("Recursive result:", binary_search_recursive(nums, target))

    missing_target = 6
    print("Searching for missing value", missing_target, "->",
          binary_search_iterative(nums, missing_target))
