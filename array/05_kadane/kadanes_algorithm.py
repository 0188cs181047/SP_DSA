"""
Maximum Subarray Sum (Kadane's Algorithm) - DP / Greedy, one pass   (Difficulty: Medium)
Asked at: Amazon, Microsoft, LinkedIn

Problem:
Given an array of integers (which may include negative numbers), find the
contiguous subarray (containing at least one number) which has the largest
sum, and return that sum.

Example:
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6   (subarray [4, -1, 2, 1])

Approach:
- Walk the array once, keeping a running sum "current" of the best subarray
  ending at the current index.
- If "current" ever drops below 0, it can only drag down any future
  subarray, so reset it to 0 (equivalently: start a fresh subarray here).
- After including each element, update a running "best" with the max seen
  so far. That way the reset happens after the update, so a subarray of a
  single very negative element is still captured correctly.
- Edge case: if every number is negative, the algorithm still works because
  we take the max *before* resetting, so the best single (least negative)
  element wins.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def max_subarray_sum(nums):
    best = nums[0]
    current = 0

    for num in nums:
        current += num
        best = max(best, current)
        if current < 0:
            current = 0

    return best


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(nums))  # 6
