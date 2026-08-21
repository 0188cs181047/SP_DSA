"""
Counting Sort - Frequency Counting (non-comparison sort)   (Difficulty: Easy/Medium)
Asked at: Amazon, Google

Problem:
Given an array of integers, sort it in ascending order without comparing
elements to each other - instead, count how many times each value occurs
and use those counts to write the output directly in sorted order. Only
worth it when the range of values is bounded and not much larger than the
number of elements.

Example:
    Input:  [4, 2, 2, 8, 3, 3, 1]
    Output: [1, 2, 2, 3, 3, 4, 8]

Approach:
- Find min and max to know the value range, then build a count array
  sized to that range where count[v - min] tracks how many times value v
  appears - one pass over the input fills it in.
- Walk the count array from the smallest value to the largest and emit
  each value as many times as it was counted - since we never compare
  elements, this sidesteps the O(n log n) comparison-sort lower bound.
- Edge cases: empty input (returns immediately), all-duplicate input
  (one bucket holds everything), and negative numbers (handled by
  offsetting every value by min_val). Bad case: a huge value range (e.g.
  one stray value of 10^9) blows up the count array, so this only pays
  off when the range k is close to n.

Time Complexity:  O(n + k), where k is the value range (max - min + 1)
Space Complexity: O(n + k) for the count array and output
"""


def counting_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    count = [0] * (max_val - min_val + 1)

    for num in arr:
        count[num - min_val] += 1

    result = []
    for offset, freq in enumerate(count):
        result.extend([offset + min_val] * freq)

    return result


if __name__ == "__main__":
    nums = [4, 2, 2, 8, 3, 3, 1]
    print("Before:", nums)
    print("After: ", counting_sort(nums))
