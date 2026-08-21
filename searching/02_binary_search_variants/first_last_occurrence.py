"""
First and Last Occurrence of an Element in a Sorted Array - Binary Search (lower/upper bound)   (Difficulty: Medium)
Asked at: Amazon, Microsoft

Problem:
Given a sorted array of integers (which may contain duplicates) and a target value,
find the index of the first and last occurrence of that target in the array. If the
target does not exist in the array, return (-1, -1). Solve it faster than a linear
scan by using binary search.

Example:
    Input: arr = [5, 7, 7, 8, 8, 8, 10], target = 8
    Output: (3, 5)

Approach:
- Run two separate binary searches instead of one: a "find first" search and a
  "find last" search, each biased in a different direction on a match.
- For first occurrence: when arr[mid] == target, record mid as a candidate but keep
  searching the LEFT half (high = mid - 1) in case an earlier occurrence exists.
- For last occurrence: when arr[mid] == target, record mid as a candidate but keep
  searching the RIGHT half (low = mid + 1) in case a later occurrence exists.
- Edge cases: target missing entirely, target appearing exactly once, target
  occupying the whole array, and empty input array.

Time Complexity:  O(log n) - two independent binary searches
Space Complexity: O(1)
"""


def find_first(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def find_last(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def first_and_last_occurrence(arr, target):
    first = find_first(arr, target)
    if first == -1:
        return (-1, -1)
    last = find_last(arr, target)
    return (first, last)


if __name__ == "__main__":
    arr = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"First and last occurrence: {first_and_last_occurrence(arr, target)}")

    missing_target = 6
    print(f"Target: {missing_target}")
    print(f"First and last occurrence: {first_and_last_occurrence(arr, missing_target)}")
