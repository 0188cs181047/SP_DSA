"""
Rotate Array by K Steps - Cyclic Replacement / Reversal   (Difficulty: Medium)
Asked at: Microsoft, Amazon

Problem:
Given an array of integers, rotate it to the right by k steps, in place,
using only constant extra space. Rotating right by one step means every
element moves one position to the right, and the last element wraps around
to the front.

Example:
    Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]

    Reversal trick:
        reverse whole array:      [7, 6, 5, 4, 3, 2, 1]
        reverse first k=3:        [5, 6, 7, 4, 3, 2, 1]
        reverse remaining n-k=4:  [5, 6, 7, 1, 2, 3, 4]

Approach:
- Normalize k with k %= n first, since rotating by a multiple of n is a
  no-op and k can be larger than the array length.
- Reverse the entire array, then reverse the first k elements, then reverse
  the remaining n - k elements. Reversing the whole thing puts the correct
  final elements at each end in the wrong internal order; re-reversing each
  of the two segments fixes their internal order while keeping them in
  their new (rotated) positions - all done in place with three linear
  passes.
- Edge cases: k == 0 or k == n after the modulo reduces to zero rotation
  (the middle reverse becomes a no-op); arrays of length 0 or 1 are
  unaffected by any rotation.

Time Complexity:  O(n) - three linear passes over the array
Space Complexity: O(1) - all reversals are done in place
"""


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return nums

    k %= n
    if k == 0:
        return nums

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Input:", nums, "k =", k)
    print("Rotated:", rotate(nums, k))

    nums = [-1, -100, 3, 99]
    k = 2
    print("Input:", nums, "k =", k)
    print("Rotated:", rotate(nums, k))
