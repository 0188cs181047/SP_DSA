"""
Find the Missing Number in an Array Containing 1 to N - Sum Formula or XOR   (Difficulty: Easy/Medium)
Asked at: Amazon, Microsoft, TCS

Problem:
Given an array containing n distinct numbers taken from the range 1 to
n + 1 with exactly one number missing, find the missing number.

Example:
    Input: nums = [1, 2, 4, 5, 6]
    Output: 3

Approach:
- Sum formula: the numbers 1..n should sum to n * (n + 1) // 2. Subtract
  the actual sum of the array from this expected sum - the difference is
  exactly the missing number. Here n is len(nums) + 1 since one number
  is absent from the array.
- XOR alternative: XOR is its own inverse (a ^ a = 0), so XOR-ing every
  number from 1..n together with every number in the array cancels out
  every value that appears in both, leaving only the missing number. This
  avoids any risk of integer overflow in languages with fixed-width ints
  (not a concern in Python, but worth mentioning), and uses only bitwise
  operations.
- Edge case: works correctly whether the missing number is at the low end
  (1), the high end (n), or anywhere in between.

Time Complexity:  O(n) for both approaches
Space Complexity: O(1)
"""


def find_missing_sum(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def find_missing_xor(nums):
    n = len(nums) + 1
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
    return xor_all


if __name__ == "__main__":
    nums = [1, 2, 4, 5, 6]
    print("nums =", nums)
    print("Missing number (sum formula):", find_missing_sum(nums))
    print("Missing number (XOR):        ", find_missing_xor(nums))
