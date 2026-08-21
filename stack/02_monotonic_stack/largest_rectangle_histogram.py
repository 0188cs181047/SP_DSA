"""
Largest Rectangle in Histogram - Monotonic Stack   (Difficulty: Hard)
Asked at: Google, Amazon, Uber

Problem:
Given an array of non-negative integers representing the heights of bars in a
histogram (each bar has width 1, placed side by side), find the area of the
largest rectangle that can be formed within the histogram's outline.

Example:
    Input:  [2, 1, 5, 6, 2, 3]
    Output: 10

    heights:      1
                  |
              5 6 |
              | | |
        2   2 | | | 3
        |   | | | | |
        -----------------
        0   1 2 3 4 5

    The tallest rectangle uses bars at indices 2 and 3 (heights 5 and 6),
    limited by the shorter one: height 5 * width 2 = 10.

Approach:
- For every bar, the largest rectangle that uses it as the limiting height
  extends left and right until it hits a shorter bar - so the key is finding,
  for each bar, how far it can stretch in both directions.
- Maintain a stack of indices with strictly increasing heights. When the
  current bar is shorter than the bar on top of the stack, that taller bar
  can no longer extend any further right, so pop it and finalize its
  rectangle: its height times the width between the new stack top (its left
  boundary) and the current index (its right boundary).
- Append a sentinel height of 0 at the end so every remaining bar on the
  stack gets flushed and its rectangle is computed.
- Each index is pushed once and popped once, giving linear total work despite
  the nested loop.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def largest_rectangle_area(heights):
    stack = []  # indices with strictly increasing heights
    max_area = 0

    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            width = i - left
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(f"Input:  {heights}")
    print(f"Output: {largest_rectangle_area(heights)}")
