"""
Next Greater Element - Monotonic Stack   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Bloomberg

Problem:
Given an array of integers, find the next greater element for each element in
the array. The next greater element of an element x is the first element to
its right that is greater than x. If no such element exists, use -1 for that
position.

Example:
    Input: [4, 5, 2, 10, 8]
    Output: [5, 10, 10, -1, -1]

Approach:
- Walk the array from right to left, since the "next greater" for index i can
  only be resolved once everything to its right is already known.
- Maintain a stack of candidate values in decreasing order. Before pushing the
  current value, pop off every stack value that is <= it, since those values
  can never be the next-greater answer for anything further left (the current,
  larger value would always win first).
- Whatever remains on top of the stack after popping is the next greater
  element for the current index; if the stack is empty, there is none (-1).
- Every element is pushed once and popped at most once, so the stack work is
  amortized O(1) per element.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def next_greater_elements(nums):
    result = [-1] * len(nums)
    stack = []  # values, kept in decreasing order from bottom to top

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])

    return result


if __name__ == "__main__":
    nums = [4, 5, 2, 10, 8]
    print(f"Input:  {nums}")
    print(f"Output: {next_greater_elements(nums)}")
