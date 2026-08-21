"""
Find the Maximum and Minimum Element in an Array - Single Pass   (Difficulty: Easy)
Asked at: Amazon, TCS, Infosys, Capgemini

Problem:
Given an array of integers, find the maximum and minimum values contained in it.
The array can have any order of elements and may contain duplicates or negative numbers.
Do this without sorting the array, since sorting costs more than necessary for this task.

Example:
    Input: [12, 45, 2, 41, 31, 10, 8]
    Output: max = 45, min = 2

Approach:
- Walk the array once, keeping two running values: the largest and smallest seen so far.
- Seed both trackers with the first element, then compare every later element against
  both trackers, updating whichever one it beats.
- A single comparison pass is O(n) and needs no extra memory beyond the two trackers.
- A well-known variant compares elements in pairs against each other first, then checks
  the larger of the pair against the running max and the smaller against the running min.
  That cuts the total comparisons from ~2n down to ~3n/2, which can matter when comparisons
  are expensive, though it is rarely needed in practice and adds bookkeeping complexity.
- Edge cases: an array with a single element (max and min are both that element) and an
  array with all equal elements (max and min end up equal too).

Time Complexity:  O(n) - every element is visited exactly once
Space Complexity: O(1) - only two extra variables are used regardless of input size
"""


def find_max_min(arr):
    current_max = arr[0]
    current_min = arr[0]

    for num in arr[1:]:
        if num > current_max:
            current_max = num
        elif num < current_min:
            current_min = num

    return current_max, current_min


if __name__ == "__main__":
    nums = [12, 45, 2, 41, 31, 10, 8]
    max_val, min_val = find_max_min(nums)
    print("Array:", nums)
    print("Max:", max_val)
    print("Min:", min_val)
