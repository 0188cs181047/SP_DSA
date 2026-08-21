"""
Next Permutation - In-place Array Manipulation   (Difficulty: Medium)
Asked at: Amazon, Google

Problem:
Given an array of integers representing a permutation of numbers, rearrange
it into the lexicographically next greater permutation of those numbers,
in place, using only constant extra space. If no such permutation exists
(the array is already the highest permutation), rearrange it into the
lowest possible order (sorted ascending) instead.

Example:
    Input:  nums = [1, 2, 3]
    Output: [1, 3, 2]

    Input:  nums = [3, 2, 1]
    Output: [1, 2, 3]   (wraps around to the smallest permutation)

Approach:
- Scan from the right to find the rightmost index i where nums[i] < nums[i+1]
  (the "pivot"). Everything to the right of i is currently in descending
  order, meaning that suffix is already the largest permutation possible
  for those elements.
- If no such pivot exists, the whole array is descending, i.e. it is the
  last permutation, so simply reverse it to wrap around to the first
  (smallest) permutation.
- Otherwise, scan from the right again to find the rightmost index j where
  nums[j] > nums[i] (the smallest value in the suffix that is still bigger
  than the pivot), swap nums[i] and nums[j], then reverse the suffix after
  i. Reversing turns the descending suffix into ascending order, which is
  the smallest arrangement of those remaining values, giving the overall
  next permutation.
- Edge cases: arrays of length 0 or 1 have only one permutation, so the
  pivot search simply finds nothing and the reverse step is a no-op.

Time Complexity:  O(n) - each element is visited a constant number of times
Space Complexity: O(1) - all work is done in place
"""


def next_permutation(nums):
    n = len(nums)

    # Step 1: find the rightmost ascent nums[i] < nums[i + 1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: find the rightmost element greater than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: reverse the suffix after i (whole array if no pivot was found)
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


if __name__ == "__main__":
    nums = [1, 2, 3]
    print("Input:", nums)
    print("Next permutation:", next_permutation(nums))

    nums = [3, 2, 1]
    print("Input:", nums)
    print("Next permutation:", next_permutation(nums))

    nums = [1, 1, 5]
    print("Input:", nums)
    print("Next permutation:", next_permutation(nums))
