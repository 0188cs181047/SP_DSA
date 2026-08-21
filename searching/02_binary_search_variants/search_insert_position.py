"""
Search Insert Position (Lower Bound) - Binary Search   (Difficulty: Easy)
Asked at: Amazon, Google

Problem:
Given a sorted array of distinct integers and a target value, return the index of
the target if it is found. If it is not found, return the index where it would be
inserted to keep the array sorted.

Example:
    Input: arr = [1, 3, 5, 6], target = 5
    Output: 2

    Input: arr = [1, 3, 5, 6], target = 2
    Output: 1

Approach:
- This is a lower-bound binary search: find the leftmost index where target could
  be placed without breaking the sorted order.
- Keep two pointers low and high. Whenever arr[mid] < target, the answer must lie
  to the right, so move low = mid + 1. Otherwise shrink high = mid - 1.
- When the loop ends, low is exactly the insertion index - it works whether the
  target is present in the array or not, so no special-casing is needed.
- Edge cases: target smaller than every element (insert at 0), target larger than
  every element (insert at len(arr)), and an empty array.

Time Complexity:  O(log n)
Space Complexity: O(1)
"""


def search_insert(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


if __name__ == "__main__":
    arr = [1, 3, 5, 6]

    target = 5
    print(f"Array: {arr}, target: {target}")
    print(f"Insert position: {search_insert(arr, target)}")

    target = 2
    print(f"Array: {arr}, target: {target}")
    print(f"Insert position: {search_insert(arr, target)}")

    target = 7
    print(f"Array: {arr}, target: {target}")
    print(f"Insert position: {search_insert(arr, target)}")
