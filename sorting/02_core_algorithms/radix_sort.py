"""
Radix Sort - Digit-by-Digit Bucketing (non-comparison sort)   (Difficulty: Medium)
Asked at: Amazon, Google

Problem:
Given an array of non-negative integers, sort it in ascending order
without comparing elements directly - instead, sort repeatedly by each
decimal digit, from least significant to most significant.

Example:
    Input:  [170, 45, 75, 90, 802, 24, 2, 66]
    Output: [2, 24, 45, 66, 75, 90, 170, 802]

Approach:
- For each digit place (1s, 10s, 100s, ...) up to the number of digits
  in the largest element, run a stable counting sort keyed on that
  digit. Because counting sort is stable, elements that tie on the
  current digit keep the relative order established by the previous
  (less significant) digit pass.
- After processing every digit place, the array is fully sorted - the
  most significant digit pass is the one that finally breaks all ties.
- Edge cases: empty input (returns immediately), all-zero/duplicate
  input (single digit pass suffices). Only works directly on
  non-negative integers; negatives need separate handling (e.g. sort
  magnitudes separately and merge).

Time Complexity:  O(d * (n + b)), d = number of digits, b = base (10)
Space Complexity: O(n + b) for the counting-sort buckets and output
"""


def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        _counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def _counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for d in range(1, 10):
        count[d] += count[d - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    for i in range(n):
        arr[i] = output[i]


if __name__ == "__main__":
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Before:", nums)
    radix_sort(nums)
    print("After: ", nums)
