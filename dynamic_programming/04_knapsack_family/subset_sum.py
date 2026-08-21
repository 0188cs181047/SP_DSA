"""
Subset Sum - Boolean 2D DP (Knapsack Variant)   (Difficulty: Medium)
Asked at: Amazon, Microsoft

Problem:
Given an array of non-negative integers and a target sum, determine whether
some subset of the array adds up to exactly that target. You don't need to
return the subset itself, just whether one exists.

Example:
    Input: nums = [3, 34, 4, 12, 5, 2], target = 9
    Output: True   (4 + 5 = 9)

Approach:
- dp[i][s] = True if some subset of the first i numbers sums to exactly s.
- dp[i][s] = dp[i-1][s] (skip nums[i-1]) OR, if nums[i-1] <= s,
  dp[i-1][s - nums[i-1]] (take nums[i-1]).
- Base case: dp[i][0] = True for every i, since the empty subset always
  sums to 0 regardless of how many numbers are available.
- Edge cases: target 0 is trivially True, and a number larger than the
  target can never be part of the subset that reaches it.

Time Complexity:  O(n * target)
Space Complexity: O(n * target)
"""


def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        num = nums[i - 1]
        for s in range(1, target + 1):
            dp[i][s] = dp[i - 1][s]
            if num <= s:
                dp[i][s] = dp[i][s] or dp[i - 1][s - num]

    return dp[n][target]


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(subset_sum(nums, target))  # True

    no_subset_nums = [1, 2, 5]
    no_subset_target = 4
    print(subset_sum(no_subset_nums, no_subset_target))  # False
