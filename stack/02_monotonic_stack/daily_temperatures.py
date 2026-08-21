"""
Daily Temperatures - Monotonic Stack of Indices   (Difficulty: Medium)
Asked at: Amazon, Google

Problem:
Given a list of daily temperatures, return a list where each position holds
the number of days you would have to wait after that day to see a strictly
warmer temperature. If there is no future day with a warmer temperature, put
0 in that position instead.

Example:
    Input:  [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [1, 1, 4, 2, 1, 1, 0, 0]

Approach:
- Scan left to right while keeping a stack of indices whose "warmer day" has
  not been found yet.
- For each new day, pop every index on the stack whose temperature is lower
  than today's temperature - today is the answer for all of them, and the
  wait time is simply the difference between the current index and the
  popped index.
- Push the current index once the stack no longer has anything smaller on
  top; it will sit there until a future warmer day resolves it (or it stays
  unresolved and keeps the default 0).
- Each index is pushed once and popped at most once, so the total work across
  the scan is linear despite the nested while loop.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # indices waiting for a warmer future day

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)

    return result


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Input:  {temperatures}")
    print(f"Output: {daily_temperatures(temperatures)}")
