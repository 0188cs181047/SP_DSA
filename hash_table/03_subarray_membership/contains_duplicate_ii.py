"""
Contains Duplicate II (within distance k) - HashMap of last-seen index   (Difficulty: Easy)
Asked at: Amazon, Google

Problem:
Given an integer array nums and an integer k, return True if there are
two distinct indices i and j in the array such that nums[i] == nums[j]
and the absolute difference between i and j is at most k.

Example:
    Input: nums = [1, 2, 3, 1, 2, 3], k = 2
    Output: False

    Input: nums = [1, 0, 1, 1], k = 1
    Output: True

Approach:
- Walk the array once, keeping a dict that maps each value to the last
  index at which it was seen - no need to store every past index, only
  the most recent one, since that is always the closest candidate.
- At index i, if nums[i] is already in the dict, the previous index it
  was seen at is the nearest possible match; compare i - last_index to
  k right there instead of scanning backward.
- If that distance is within k, a valid pair exists - return True
  immediately without finishing the scan.
- Otherwise (or if the value hasn't been seen yet), update the dict
  with the current index so later occurrences compare against this
  more recent position.
- Edge cases: k = 0 means indices must be equal to each other, which is
  impossible for distinct i and j, so the answer is always False; an
  array shorter than 2 elements also trivially returns False.

Time Complexity:  O(n)
Space Complexity: O(min(n, k)) - at most k+1 recent indices matter, but a plain dict of all distinct values is simpler and still O(n)
"""


def contains_nearby_duplicate(nums, k):
    last_seen = {}

    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(f"Array: {nums}, k = {k}")
    print("Contains nearby duplicate:", contains_nearby_duplicate(nums, k))

    nums2 = [1, 0, 1, 1]
    k2 = 1
    print(f"\nArray: {nums2}, k = {k2}")
    print("Contains nearby duplicate:", contains_nearby_duplicate(nums2, k2))

    nums3 = [1, 2, 3, 1]
    k3 = 0
    print(f"\nArray: {nums3}, k = {k3}")
    print("Contains nearby duplicate:", contains_nearby_duplicate(nums3, k3))
