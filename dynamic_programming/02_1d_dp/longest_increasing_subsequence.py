"""
Longest Increasing Subsequence (LIS) - 1D DP, with an O(n log n) binary-search improvement   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
Given an array of integers, return the length of the longest strictly
increasing subsequence. Elements of the subsequence don't need to be
contiguous in the original array, but they must keep their original
relative order.

Example:
    Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4   (subsequence [2, 3, 7, 101] or [2, 3, 7, 18])

Approach:
- Classic O(n^2) DP: dp[i] = length of the longest increasing
  subsequence that ends exactly at index i.
  dp[i] = 1 + max(dp[j] for j < i where nums[j] < nums[i]), or 1 if no
  earlier element is smaller. The answer is max(dp).
- Faster O(n log n) version (patience sorting): keep a "tails" array
  where tails[k] is the smallest tail value among all increasing
  subsequences of length k + 1 built so far. For each new number,
  binary search (bisect_left) for where it belongs in tails - if it's
  bigger than everything, append and extend the LIS length; otherwise
  overwrite the first tail that is >= it, since a smaller tail for the
  same length keeps more future options open.
- tails is not an actual subsequence at the end, only its length
  matters - it's a bookkeeping array, not the answer itself.
- Edge cases: empty input (length 0), all duplicate values (length 1,
  since the subsequence must be strictly increasing), and an already
  sorted or strictly descending array.

Time Complexity:  O(n^2) for the DP version, O(n log n) for the binary-search version
Space Complexity: O(n) for both
"""

import bisect


def length_of_lis_dp(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def length_of_lis_binary_search(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis_dp(nums))              # 4
    print(length_of_lis_binary_search(nums))    # 4
