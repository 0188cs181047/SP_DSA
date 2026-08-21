"""
Partition Equal Subset Sum - Reduces to Subset Sum on total/2   (Difficulty: Medium)
Asked at: Amazon, Google, Meta

Problem:
Given an array of positive integers, determine whether it can be split
into two subsets so that the sum of elements in each subset is equal.
Every element must belong to exactly one of the two subsets.

Example:
    Input: nums = [1, 5, 11, 5]
    Output: True   ([1, 5, 5] and [11] both sum to 11)

Approach:
- If the two subsets have equal sums, each one must sum to exactly
  total_sum / 2, so the total sum must be even - if it's odd, splitting
  evenly is impossible and the answer is False immediately.
- This turns the problem into plain Subset Sum: does some subset of nums
  sum to exactly total_sum // 2? If so, the leftover elements automatically
  sum to the other half too.
- Use a 1D boolean DP: dp[s] = True if some subset seen so far sums to s.
  Iterate the target range backwards for each number so that each item is
  only used once (the classic 0/1 knapsack trick for a 1D array).
- Edge cases: an empty array (sum 0, trivially partitionable into two empty
  halves) and a single element (never partitionable unless it's 0).

Time Complexity:  O(n * total_sum)
Space Complexity: O(total_sum)
"""


def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

    return dp[target]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(can_partition(nums))  # True

    odd_sum_nums = [1, 2, 3, 5]
    print(can_partition(odd_sum_nums))  # False
