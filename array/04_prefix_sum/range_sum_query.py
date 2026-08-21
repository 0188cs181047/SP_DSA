"""
Range Sum Query - Immutable - Prefix Sum   (Difficulty: Easy)
Asked at: Amazon, Google

Problem:
Design a class that is given an integer array nums and must answer many
sumRange(left, right) queries, each returning the sum of the elements
between indices left and right inclusive. The array itself never changes
between queries.

Example:
    Input:
        nums = [-2, 0, 3, -5, 2, -1]
        sumRange(0, 2) -> 1    (-2 + 0 + 3)
        sumRange(2, 5) -> -1   (3 + -5 + 2 + -1)
        sumRange(0, 5) -> -3   (sum of the whole array)
    Output: 1, -1, -3

    index:    0   1   2   3   4   5
    nums:    -2   0   3  -5   2  -1
    prefix:  0  -2  -2   1  -4  -2  -3
             (prefix[i] = sum of nums[0..i-1], one extra slot up front)

Approach:
- Since the array is immutable and queries can be repeated many times,
  precompute a prefix-sum array once in the constructor: prefix[i] holds
  the sum of nums[0..i-1], with prefix[0] = 0 as a sentinel.
- Answer any query in O(1) as prefix[right + 1] - prefix[left] - this is
  just "total up to right" minus "total up to left", which cancels out
  everything before index left and leaves exactly nums[left..right].
- The sentinel prefix[0] = 0 means left = 0 needs no special casing;
  it naturally subtracts nothing.
- Trade a bit of extra space and one-time O(n) setup for O(1) queries,
  which is worth it whenever queries greatly outnumber array updates.

Time Complexity:  O(n) to build, O(1) per query
Space Complexity: O(n) for the prefix-sum array
"""


class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sum_range(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)

    print(f"Array: {nums}")
    print("sumRange(0, 2):", num_array.sum_range(0, 2))
    print("sumRange(2, 5):", num_array.sum_range(2, 5))
    print("sumRange(0, 5):", num_array.sum_range(0, 5))
