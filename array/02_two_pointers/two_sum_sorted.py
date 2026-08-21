"""
Two Sum II - Pair with Target Sum in a Sorted Array - Two Pointers   (Difficulty: Easy)
Asked at: Amazon, Microsoft, Google

Problem:
Given an array of integers sorted in ascending order and a target value, find
the indices of the two numbers that add up to the target. Return the indices
(1-indexed, as is typical for this variant) of the two numbers. Assume exactly
one valid answer exists and you may not use the same element twice.

Example:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]   (numbers[0] + numbers[1] == 9)

Approach:
- Because the array is already sorted, a left pointer at the start and a
  right pointer at the end let us reason about the sum directly: if the sum
  is too small, the only way to grow it is to move left forward; if it's too
  big, the only way to shrink it is to move right backward.
- This converges in a single pass since the pointers only ever move toward
  each other, giving O(n) time and O(1) extra space.
- Contrast with the classic (unsorted) Two Sum problem, which needs a hashmap
  of value -> index and O(n) space because there's no ordering to exploit;
  here the sortedness is exactly what lets us drop the hashmap.
- Edge cases: duplicate values still work fine since we only ever move one
  pointer at a time based on the sum comparison; a two-element array is the
  minimal valid input.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum_sorted(numbers, target))
