"""
Subarray Sum Equals K - Prefix Sum + HashMap   (Difficulty: Medium)
Asked at: Google, Meta, Amazon

Problem:
Given an array of integers nums and an integer k, return the total number
of contiguous subarrays whose elements sum up to exactly k. The array may
contain negative numbers, zero, and positive numbers.

Example:
    Input: nums = [1, 1, 1], k = 2
    Output: 2   (the subarrays [1, 1] at indices [0,1] and [1,2])

The subarray sum from index j+1 to i equals prefix[i] - prefix[j], where
prefix[i] is the running sum of nums[0..i]. So for every index i we just
need to know how many earlier prefix sums equal (prefix[i] - k):

    nums:    1    1    1
    prefix:  1    2    3
    at i=1 (prefix=2): need prefix-k=0 -> seen once (the empty prefix) -> +1
    at i=2 (prefix=3): need prefix-k=1 -> seen once (index 0)          -> +1

Approach:
- Walk the array once, keeping a running prefix sum and a dict that maps
  each prefix-sum value seen so far to how many times it has occurred.
- For the current prefix sum, the number of valid subarrays ending at the
  current index equals sum_freq.get(prefix_sum - k, 0) - every earlier
  index with that prefix sum marks the start of a subarray summing to k.
- Seed the dict with {0: 1} before the loop so subarrays that start at
  index 0 (where there is no "earlier" prefix) are counted correctly.
- Update the frequency dict for the current prefix sum after using it to
  count, so a subarray never counts itself against itself.
- Works fine with negative numbers and zeros since it never assumes the
  prefix sum is monotonic (unlike a sliding-window approach).

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}

    for num in nums:
        prefix_sum += num
        count += sum_freq.get(prefix_sum - k, 0)
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(f"Array: {nums}, k = {k}")
    print("Number of subarrays summing to k:", subarray_sum(nums, k))

    nums2 = [1, 2, 3, -3, 1, 1]
    k2 = 3
    print(f"\nArray: {nums2}, k = {k2}")
    print("Number of subarrays summing to k:", subarray_sum(nums2, k2))
