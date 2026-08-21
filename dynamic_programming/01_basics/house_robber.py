"""
House Robber - 1D DP (include/exclude current element)   (Difficulty: Easy/Medium)
Asked at: Amazon, Google, Meta

Problem:
You are a robber planning to rob houses along a street. Each house has some
amount of money, given in the array nums. Adjacent houses share a connected
security system - if two adjacent houses are robbed on the same night the
alarm goes off. Return the maximum amount of money you can rob without ever
robbing two adjacent houses.

Example:
    Input: nums = [2, 7, 9, 3, 1]
    Output: 12  (rob houses at index 0, 2, 4: 2 + 9 + 1 = 12)

Approach:
- For each house i there are exactly two choices: skip it and keep the best
  total achievable through house i-1, or rob it and add its value to the
  best total achievable through house i-2 (house i-1 must then be left
  alone). That gives dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
- dp only ever looks back two steps, so the full array isn't needed - two
  rolling variables (best-through-previous-house, best-through-two-houses-ago)
  are enough, dropping space from O(n) to O(1).
- Edge cases: an empty list of houses robs for 0; a single house just robs
  that house's value.

Time Complexity:  O(n)
Space Complexity: O(1) for the rolling version (O(n) for the plain dp-array version shown for clarity)
"""


def house_robber_dp_array(nums):
    # Straightforward dp array version - easiest to reason about first.
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]


def house_robber(nums):
    # O(1) space: only the previous two dp values are ever needed.
    prev2, prev1 = 0, 0  # best total through "house -2" and "house -1"
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(f"DP array version: house_robber_dp_array({nums}) = {house_robber_dp_array(nums)}")
    print(f"O(1) space:       house_robber({nums}) = {house_robber(nums)}")
