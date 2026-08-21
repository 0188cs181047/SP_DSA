"""
Top K Frequent Elements - HashMap + Heap / Bucket Sort   (Difficulty: Medium)
Asked at: Amazon, Meta, Google

Problem:
Given an integer array nums and an integer k, return the k most
frequently occurring elements in the array. The answer may be returned
in any order, and it is guaranteed that the answer is unique.

Example:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

    nums:   1  1  1  2  2  3
    freq:   1 -> 3, 2 -> 2, 3 -> 1
    bucket: index 1 -> [3]   (elements seen exactly once)
            index 2 -> [2]   (elements seen exactly twice)
            index 3 -> [1]   (elements seen exactly three times)
    read buckets from the back (highest frequency first) until k
    elements are collected -> [1, 2]

Approach:
- First pass: count how often each element occurs using a dict - this
  is the frequency table every solution below builds on.
- Heap approach: push (frequency, element) onto a min-heap capped at
  size k (heapq.nlargest works too); the k elements left on the heap
  are the k most frequent, giving O(n log k).
- Bucket-sort approach used here: since frequency can range only from
  1 to n, create n+1 buckets indexed by frequency and drop each element
  into the bucket matching its count. Reading buckets from the highest
  index down and collecting elements gives the top k in O(n) overall,
  because sorting by comparison is avoided entirely.
- Stop as soon as k elements have been collected - no need to drain
  every bucket once the answer is complete.
- Edge case: if k equals the number of distinct elements, every bucket
  eventually gets read and all distinct elements are returned.

Time Complexity:  O(n)
Space Complexity: O(n)
"""

from collections import Counter


def top_k_frequent(nums, k):
    freq = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    result = []
    for count in range(len(buckets) - 1, 0, -1):
        for num in buckets[count]:
            result.append(num)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"Array: {nums}, k = {k}")
    print("Top k frequent elements:", top_k_frequent(nums, k))

    nums2 = [7]
    k2 = 1
    print(f"\nArray: {nums2}, k = {k2}")
    print("Top k frequent elements:", top_k_frequent(nums2, k2))
