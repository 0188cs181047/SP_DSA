"""
Search in a Rotated Sorted Array - Modified Binary Search   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Google, Bloomberg

Problem:
An array that was originally sorted in ascending order has been rotated at some
unknown pivot (e.g. [4, 5, 6, 7, 0, 1, 2]). Given the rotated array and a target
value, find the index of the target in O(log n) time. Return -1 if it is not
present. Assume all elements are distinct.

Example:
    Input: arr = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

    Input: arr = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1

    arr:   [4, 5, 6, 7, 0, 1, 2]
    idx:    0  1  2  3  4  5  6
                       ^-- pivot (rotation point)

Approach:
- At every step, one of the two halves around mid (low..mid or mid..high) is
  always a normal ascending run, even though the whole array is not.
- Compare arr[low], arr[mid], arr[high] to decide which half is the sorted one:
  if arr[low] <= arr[mid], the left half is sorted; otherwise the right half is.
- Once the sorted half is known, check whether target falls within that half's
  value range. If it does, search there; otherwise search the other half.
- Edge cases: no rotation at all (fully sorted array), single-element array,
  target equal to arr[low]/arr[high], and target absent entirely.

Time Complexity:  O(log n)
Space Complexity: O(1)
"""


def search_rotated(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            # left half (low..mid) is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # right half (mid..high) is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]

    target = 0
    print(f"Array: {arr}, target: {target}")
    print(f"Index: {search_rotated(arr, target)}")

    target = 3
    print(f"Array: {arr}, target: {target}")
    print(f"Index: {search_rotated(arr, target)}")
