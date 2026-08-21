"""
First Negative Number in Every Window of Size K - Deque of Indices   (Difficulty: Medium)
Asked at: Amazon, Adobe

Problem:
Given an array of integers `nums` and a window size `k`, slide a window of
size k from left to right one step at a time. For each window, report the
first negative number that appears in it, or 0 if the window has no
negative numbers.

Example:
    Input:  nums = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
    Output: [-1, -1, -7, -15, -15, 0]

Approach:
- Keep a deque that stores only the indices of negative numbers that are
  currently inside the window, in the order they were seen. Because it
  only ever gets appended to at the back and trimmed at the front, the
  front is always the earliest (i.e. first) negative number in the
  window.
- When the window slides past an index (index <= current_index - k),
  pop it from the front of the deque if it's there - it's no longer in
  play for future windows.
- For each new element, push its index onto the back of the deque only
  if the element is negative; positive/zero elements never affect the
  answer and are skipped entirely.
- Once the window has filled up for the first time, the answer for that
  window is nums[deque[0]] if the deque is non-empty, otherwise 0.
- Edge case: a window with no negative numbers at all leaves the deque
  empty, which is exactly when we report 0.

Time Complexity:  O(n) - each index enters and leaves the deque at most once
Space Complexity: O(k) - the deque holds at most k indices at a time
"""

from collections import deque


def first_negative_in_window(nums, k):
    result = []
    negatives = deque()  # indices of negative numbers inside the window

    for i, num in enumerate(nums):
        if num < 0:
            negatives.append(i)

        # drop the front index once it's outside the current window
        if negatives and negatives[0] <= i - k:
            negatives.popleft()

        # window has filled up for the first time at i == k - 1
        if i >= k - 1:
            result.append(nums[negatives[0]] if negatives else 0)

    return result


if __name__ == "__main__":
    nums = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    print("nums:", nums)
    print("k:", k)
    print("first negative per window:", first_negative_in_window(nums, k))
    # [-1, -1, -7, -15, -15, 0]
