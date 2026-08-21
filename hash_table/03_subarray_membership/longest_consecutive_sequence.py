"""
Longest Consecutive Sequence - HashSet   (Difficulty: Medium)
Asked at: Amazon, Meta, Google

Problem:
Given an unsorted array of integers, find the length of the longest run
of consecutive integers (not necessarily contiguous in the array, and
not necessarily sorted to begin with). The array may contain duplicates.

Example:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4

    set:            {100, 4, 200, 1, 3, 2}
    1 has no 0 in set -> start of a run: 1, 2, 3, 4 -> length 4
    100 has no 99 in set -> start of a run: 100 -> length 1
    200 has no 199 in set -> start of a run: 200 -> length 1
    longest run found -> 4

Approach:
- Dump every number into a set first - this gives O(1) membership
  checks and automatically collapses duplicates, which would otherwise
  inflate a naive run count.
- Sorting and scanning would work but costs O(n log n); the set trick
  gets to O(n) by only ever starting a count from the true beginning
  of a run.
- A number n is the start of a run only if n - 1 is NOT in the set -
  checking this before counting upward guarantees each run is counted
  exactly once, from its start, instead of once per element in it.
- From a valid start, keep checking n + 1, n + 2, ... while they exist
  in the set, extending the length each time, and track the best
  length seen across all starts.
- Edge cases: empty input returns 0; an array with no two consecutive
  numbers returns 1 (every element is its own run of length 1).

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 in num_set:
            continue  # not the start of a run, skip it

        length = 1
        current = num
        while current + 1 in num_set:
            current += 1
            length += 1

        longest = max(longest, length)

    return longest


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(f"Array: {nums}")
    print("Longest consecutive sequence length:", longest_consecutive(nums))

    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"\nArray: {nums2}")
    print("Longest consecutive sequence length:", longest_consecutive(nums2))

    nums3 = []
    print(f"\nArray: {nums3}")
    print("Longest consecutive sequence length:", longest_consecutive(nums3))
