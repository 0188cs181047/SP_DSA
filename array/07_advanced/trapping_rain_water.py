"""
Trapping Rain Water - Two Pointers / Precomputed Max Arrays   (Difficulty: Hard)
Asked at: Google, Amazon, Adobe

Problem:
You are given an array of non-negative integers representing the height of
bars in a histogram, each of width 1. After it rains, water gets trapped
between the bars. Compute how much water is trapped in total.

Example:
    Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

    Cross-section (# = bar, ~ = trapped water):
        3           #
        2     #  ~~~#~#
        1  ~ #~~#~~~#~#~#
        0  #~#~#~~~~~~~~~
           0 1 2 3 4 5 6 7 8 9 ...

Approach:
- Water trapped above index i is limited by the shorter of the tallest bar
  to its left and the tallest bar to its right: water[i] = min(maxLeft[i],
  maxRight[i]) - height[i] (never negative).
- O(n) extra-space version: precompute maxLeft[] and maxRight[] arrays in
  two passes, then sum the trapped water in a third pass.
- O(1) extra-space version: walk two pointers inward from both ends,
  tracking the running max seen from the left and from the right. Whichever
  side currently has the smaller running max is the side that determines
  the trapped water at that pointer, because the far side is guaranteed to
  have at least that much height somewhere beyond it.
- Edge cases: arrays of length 0, 1, or 2 can never trap water and should
  return 0 immediately (the two-pointer loop handles this naturally).

Time Complexity:  O(n) for both versions
Space Complexity: O(n) for the precomputed-array version, O(1) for the two-pointer version
"""


def trap_with_extra_space(height):
    n = len(height)
    if n < 3:
        return 0

    max_left = [0] * n
    max_right = [0] * n

    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i])

    max_right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i])

    total = 0
    for i in range(n):
        total += min(max_left[i], max_right[i]) - height[i]
    return total


def trap(height):
    n = len(height)
    if n < 3:
        return 0

    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    total = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            total += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total += right_max - height[right]

    return total


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("Input:", height)
    print("Trapped water (extra space):", trap_with_extra_space(height))
    print("Trapped water (two pointer):", trap(height))
