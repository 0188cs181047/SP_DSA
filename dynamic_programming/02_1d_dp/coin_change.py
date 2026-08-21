"""
Coin Change (Minimum Number of Coins) - Unbounded Knapsack / 1D DP   (Difficulty: Medium)
Asked at: Amazon, Google, Uber

Problem:
Given an array of coin denominations and a target amount, find the fewest
number of coins needed to make up that amount. Each coin denomination can
be used an unlimited number of times. If no combination of coins can make
up the amount, return -1.

Example:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3   (11 = 5 + 5 + 1)

Approach:
- Bottom-up DP over amounts: dp[a] = minimum number of coins needed to
  make up amount a.
- Base case dp[0] = 0 (zero coins are needed to make amount 0).
- For every amount a from 1 up to the target, try every coin that is
  small enough to fit (coin <= a) and take
  dp[a] = min(dp[a], 1 + dp[a - coin]).
- Any amount that is still infinity after filling the table can't be
  formed by these coins, so the answer for it is -1.
- Edge cases: amount = 0 (answer is 0), a coin exactly equal to the
  amount, and amounts that are unreachable (e.g. coins = [2], amount = 3).

Time Complexity:  O(amount * len(coins))
Space Complexity: O(amount)
"""


def coin_change(coins, amount):
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1

    return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coin_change(coins, amount))  # 3

    unreachable_coins = [2]
    unreachable_amount = 3
    print(coin_change(unreachable_coins, unreachable_amount))  # -1
