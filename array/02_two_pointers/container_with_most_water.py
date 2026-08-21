"""
Container With Most Water - Two Pointers   (Difficulty: Medium)
Asked at: Amazon, Google, Adobe

Problem:
Given an array of non-negative integers where each value represents the
height of a vertical line drawn at that index, find two lines that, together
with the x-axis, form a container that holds the most water. Return the
maximum amount of water the container can store. The width of the container
is the distance between the two chosen indices.

Example:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49   (lines at index 1 and index 8: width 7 * height min(8,7) = 49)

Approach:
- Start with the widest possible container: a left pointer at index 0 and a
  right pointer at the last index. Track the best area seen so far.
- The key insight: for any current pair, the shorter of the two lines is the
  limiting factor - moving the taller line inward can only shrink the width
  without ever increasing the height cap, so it can never improve the area.
  Moving the shorter line inward is the only move that has a chance of
  finding a taller line to increase the area, even though width shrinks.
- So at each step, compute the area, update the best, and advance whichever
  pointer points at the shorter line (advance either on a tie).
- This visits each index at most once as pointers close in, giving O(n) time
  and O(1) extra space.
- Edge cases: an array of length 2 just returns the single possible area;
  arrays with duplicate heights are handled fine since ties just pick either
  side to move.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def max_area(height):
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        best = max(best, current_area)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return best


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(height))
