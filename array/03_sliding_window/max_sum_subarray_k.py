"""
Maximum Sum Subarray of Size K - Fixed Sliding Window   (Difficulty: Easy)
Asked at: Amazon, Microsoft, TCS

Problem:
Given an array of integers and a positive integer k, find the maximum sum
of any contiguous subarray of size exactly k. Assume the array has at
least k elements.

Example:
    Input: arr = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9   (subarray [5, 1, 3])

Window slides one step at a time:
    [2 1 5] 1 3 2  -> sum 8
     2 [1 5 1] 3 2 -> sum 7
     2 1 [5 1 3] 2 -> sum 9   <- max
     2 1 5 [1 3 2] -> sum 6

Approach:
- Keep a running sum for the current window instead of re-summing it
  from scratch on every shift - that is what makes this O(n) instead
  of O(n * k).
- Slide the window by adding the incoming right element and subtracting
  the outgoing left element once the window has grown to size k.
- Track the best sum seen so far as the window moves across the array.
- Edge case: if len(arr) == k, the window never slides and the answer
  is just the sum of the whole array.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Array: {arr}, k = {k}")
    print("Maximum sum of a subarray of size k:", max_sum_subarray_k(arr, k))
