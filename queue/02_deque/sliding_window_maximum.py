"""
Sliding Window Maximum - Monotonic Deque   (Difficulty: Hard)
Asked at: Amazon, Google, Meta

Problem:
Given an array of integers `nums` and a window size `k`, slide a window of
size k from left to right across the array one step at a time. For every
position of the window, report the maximum value inside it. Do this in
better than the naive O(n*k) time.

Example:
    Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [3, 3, 5, 5, 6, 7]

    index:      0    1    2    3    4    5    6    7
    nums:     [ 1 ,  3 , -1 , -3 ,  5 ,  3 ,  6 ,  7 ]
    window @2: [ 1 ,  3 , -1 ]                          -> max 3
    window @3:      [ 3 , -1 , -3 ]                     -> max 3
    window @4:           [-1 , -3 ,  5 ]                -> max 5
    ...

    deque stores indices, values kept in decreasing order front-to-back:
    after i=0: [0]                 (values: [1])
    after i=1: [1]                 (3 pops the smaller 1 from the back)
    after i=2: [1, 2]              (-1 is smaller, just appended)
    after i=3: [1, 2, 3] -> [3]    (-3 appended, then 1 falls out of window)
    front of deque is always the index of the current window's maximum.

Approach:
- Keep a deque of indices whose corresponding values are in strictly
  decreasing order from front to back. The front index is therefore
  always the maximum of the current window.
- For each new element, pop from the back of the deque while its value
  is <= the new element - those older, smaller values can never be the
  answer for any future window that also contains the new element, so
  they are useless to keep around.
- Before recording an answer, pop from the front of the deque if its
  index has slid out of the window (index <= current_index - k).
- Only start recording the max once the window has filled up for the
  first time, i.e. once we've processed at least k elements.
- Each index is pushed and popped from the deque at most once, so the
  total work across the whole array stays linear.

Time Complexity:  O(n) - each index enters and leaves the deque once
Space Complexity: O(k) - the deque holds at most k indices at a time
"""

from collections import deque


def sliding_window_maximum(nums, k):
    result = []
    window = deque()  # indices of nums, values in decreasing order

    for i, num in enumerate(nums):
        # drop indices whose values can never win against the new one
        while window and nums[window[-1]] <= num:
            window.pop()
        window.append(i)

        # drop the front index once it's outside the current window
        if window[0] <= i - k:
            window.popleft()

        # window has filled up for the first time at i == k - 1
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("nums:", nums)
    print("k:", k)
    print("window maximums:", sliding_window_maximum(nums, k))
    # [3, 3, 5, 5, 6, 7]
