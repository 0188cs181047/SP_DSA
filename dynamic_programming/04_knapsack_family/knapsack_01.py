"""
0/1 Knapsack - 2D DP (include/exclude each item once)   (Difficulty: Medium)
Asked at: Amazon, Google

Problem:
Given the weights and values of n items and a knapsack with capacity W,
find the maximum total value you can carry. Each item can either be taken
whole or left behind entirely (no fractional items), and each item may be
used at most once.

Example:
    Input: weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7
    Output: 9   (take items with weight 3 and weight 4 -> value 4 + 5 = 9)

Approach:
- dp[i][w] = the best value achievable using only the first i items with a
  knapsack of capacity w.
- For item i, there are two choices: skip it (dp[i][w] = dp[i-1][w]), or
  take it if it fits (dp[i][w] = value[i-1] + dp[i-1][w - weight[i-1]]).
  Take whichever choice gives the larger value.
- Base case: dp[0][w] = 0 for every w (no items means no value), and
  dp[i][0] = 0 for every i (no capacity means nothing fits).
- Edge cases: an item whose weight exceeds the remaining capacity can never
  be taken at that capacity, and capacity 0 always yields 0.

Time Complexity:  O(n * capacity)
Space Complexity: O(n * capacity)
"""


def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weight <= w:
                dp[i][w] = max(dp[i][w], value + dp[i - 1][w - weight])

    return dp[n][capacity]


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print(knapsack_01(weights, values, capacity))  # 9
