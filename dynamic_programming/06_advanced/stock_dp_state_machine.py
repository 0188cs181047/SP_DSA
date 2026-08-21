"""
Best Time to Buy/Sell Stock with Cooldown / Transaction Fee - DP State Machine (holding / not-holding / cooldown)   (Difficulty: Hard)
Asked at: Amazon, Google

Problem:
Given an array of daily stock prices, find the maximum profit achievable
with unlimited transactions, subject to two rules: after you sell, you
must wait one full day (a "cooldown") before you're allowed to buy again,
and every transaction costs a flat fee. You may only hold at most one
share at a time, and you can't buy and sell on the same day.

Example:
    Input: prices = [1, 2, 3, 0, 2], fee = 1
    Output: 1   (buy at 1, sell at 3 for profit 3-1-1=1; the leftover
                 buy-at-0/sell-at-2 pair also nets only 1, and combining
                 both trades still nets 1 once cooldown and fee are paid)

Each day sits in exactly one of three states, and today's values only
depend on yesterday's:

    rest --buy (-price-fee)--> hold --sell (+price)--> sold --cooldown (1 day)--> rest

Approach:
- Model the day as a tiny state machine with three rolling values instead
  of three full DP arrays, since each day only ever needs yesterday's
  numbers:
    * hold - best profit if we are holding a share at the end of today
    * sold - best profit if we *just* sold our share today (this state
      forces a one-day cooldown before we're allowed to buy again)
    * rest - best profit if we are not holding and are free to buy today
- Transitions each day (using today's price):
    * hold = max(hold, rest - price - fee)   -> either keep holding, or
      buy today from the "free to buy" state (fee charged at purchase so
      it's counted exactly once per round trip)
    * sold = hold(prev) + price              -> sell the share we were
      holding yesterday
    * rest = max(rest(prev), sold(prev))     -> stay free to buy, or the
      cooldown from yesterday's sale has now lifted
- The answer is max(sold, rest) on the last day - ending the array while
  still holding an unsold share is never optimal, so "hold" is excluded.
- Edge cases: empty price list -> 0; a single price -> 0 (nothing to sell
  against); fee = 0 reduces this to the plain cooldown-only problem.

Time Complexity:  O(n) - one pass over the prices, constant work per day
Space Complexity: O(1) - only three rolling values are kept
"""


def max_profit_with_cooldown_and_fee(prices, fee=0):
    if not prices:
        return 0

    hold = -prices[0] - fee   # bought on day 0
    sold = float("-inf")      # can't have sold with no stock yet
    rest = 0                  # free to buy, no profit or loss yet

    for price in prices[1:]:
        prev_hold, prev_sold, prev_rest = hold, sold, rest

        hold = max(prev_hold, prev_rest - price - fee)
        sold = prev_hold + price
        rest = max(prev_rest, prev_sold)

    return max(sold, rest)


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]

    print(max_profit_with_cooldown_and_fee(prices, fee=1))  # 1
    print(max_profit_with_cooldown_and_fee(prices, fee=0))  # 3 (cooldown only)
