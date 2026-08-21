"""
Sort a Nearly Sorted (K-Sorted) Array - Min-Heap of size K+1   (Difficulty: Medium)
Asked at: Amazon, Microsoft

Problem:
You are given an array where every element is at most k positions away
from where it would sit in fully sorted order (a "k-sorted" or "nearly
sorted" array). Sort the array efficiently, doing better than a general
O(n log n) sort by exploiting the bound on displacement.

Example:
    Input: nums = [6, 5, 3, 2, 8, 10, 9], k = 3
    Output: [2, 3, 5, 6, 8, 9, 10]

Approach:
- Because no element is more than k positions from its final spot, the
  smallest remaining element must always be among the next k+1 unseen
  elements - so a min-heap that never holds more than k+1 items always
  has the true next output value sitting at its top.
- Push the first k+1 elements into the min-heap, then for every
  remaining element: pop the minimum into the result and push the new
  element, keeping the heap size steady at k+1 the whole time.
- Once the input is exhausted, drain the rest of the heap in pop-order
  to finish the result (each pop still yields the next smallest).
- Edge cases: k == 0 (array is already sorted, this just drains a
  single-element heap repeatedly), k >= len(nums) (falls back to loading
  everything and draining, equivalent to a plain heapsort).

Time Complexity:  O(n log k)
Space Complexity: O(k)
"""

import heapq


def sort_k_sorted_array(nums, k):
    min_heap = nums[:k + 1]
    heapq.heapify(min_heap)
    result = []

    for i in range(k + 1, len(nums)):
        result.append(heapq.heappushpop(min_heap, nums[i]))

    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


if __name__ == "__main__":
    nums = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    print(sort_k_sorted_array(nums, k))  # [2, 3, 5, 6, 8, 9, 10]
