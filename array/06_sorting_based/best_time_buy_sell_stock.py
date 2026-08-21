"""
Best Time to Buy and Sell Stock - One Pass / Greedy   (Difficulty: Easy)
Asked at: Amazon, Microsoft, Bloomberg

Problem:
Given an array of prices where prices[i] is the price of a stock on day i,
find the maximum profit achievable by buying on one day and selling on a
later day. You must buy before you sell, and only one transaction is
allowed. If no profit is possible, return 0.

Example:
    Input: [7, 1, 5, 3, 6, 4]
    Output: 5   (buy at 1, sell at 6)

Approach:
- Walk the array once, tracking the minimum price seen so far - this is
  the best possible day to have bought, considering only days up to now.
- At each day, compute the profit if we sold today (price - min_price_so_far)
  and keep a running max of that value across all days.
- Update min_price_so_far after checking the profit for the current day, so
  we never "buy" and "sell" on the same day using a price that comes later.
- Edge cases: a strictly decreasing price array yields 0 profit (never
  worth selling); a single-day array also yields 0 since there's no later
  day to sell on.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def max_profit(prices):
    min_price_so_far = prices[0]
    best_profit = 0

    for price in prices:
        profit_if_sold_today = price - min_price_so_far
        best_profit = max(best_profit, profit_if_sold_today)
        min_price_so_far = min(min_price_so_far, price)

    return best_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))  # 5
