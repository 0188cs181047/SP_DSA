"""
Sort Colors (Dutch National Flag) - Three Pointers   (Difficulty: Medium)
Asked at: Microsoft, Meta, Google

Problem:
Given an array containing only the values 0, 1, and 2 (representing red,
white, and blue), sort it in-place so that all 0s come first, then all 1s,
then all 2s. Do this in a single pass without using a separate counting
array or the built-in sort.

Example:
    Input: nums = [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

    low                 mid                 high
     v                   v                   v
    [0  0  1  1  2  2]  <- final partition: [0s | 1s | 2s]

Approach:
- Use three pointers: low marks the boundary after which all 0s have been
  placed, high marks the boundary before which all 2s have been placed, and
  mid scans through the unclassified middle region.
- At each step, look at nums[mid]: if it's 0, swap it down to low and advance
  both low and mid (the swapped-in value at mid is already known to be a 1,
  safe to move past); if it's 2, swap it up to high and advance only high
  (the swapped-in value still needs to be classified, so mid stays put); if
  it's 1, it's already in the right region, so just advance mid.
- This classifies every element in one pass with only pointer swaps, giving
  O(n) time and O(1) extra space - this is the classic Dutch National Flag
  partitioning scheme.
- Edge cases: an array that's already sorted, or one containing only a
  single distinct value, still terminates correctly since mid simply walks
  to the end without triggering extra swaps.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1

    return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(sort_colors(nums))
