"""
Kth Largest Element in an Array - Quickselect / Heap   (Difficulty: Medium)
Asked at: Amazon, Google, Meta, Microsoft

Problem:
Given an unsorted array of integers and an integer k, find the kth largest
element in the array. Note that it is the kth largest element in sorted
order, not the kth distinct element. You should aim for better than the
O(n log n) full-sort baseline.

Example:
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5

Approach:
- Quickselect: pick a pivot, partition the array so smaller elements land
  left and larger elements land right (like quicksort), then only recurse
  into the half that must contain the target rank - never both halves.
- Convert "kth largest" into "index n-k in ascending sorted order" and
  quickselect for that index directly, avoiding a full sort.
- Randomizing the pivot choice keeps the average case O(n) even on
  adversarial input; worst case is still O(n^2) with a bad pivot sequence.
- Alternative shown below: a min-heap of size k gives O(n log k) time and
  O(k) space, which is preferable when k is small relative to n or when
  processing a stream where n isn't known upfront.
- Edge cases: k == 1 (just the max), k == n (just the min), duplicate
  values (handled naturally since we only care about position, not
  distinctness).

Time Complexity:  O(n) average / O(n^2) worst case for quickselect, O(n log k) for the heap approach
Space Complexity: O(1) extra for in-place quickselect (recursion aside), O(k) for the heap approach
"""

import heapq
import random


def find_kth_largest_quickselect(nums, k):
    nums = nums[:]  # avoid mutating caller's list
    target_index = len(nums) - k  # index of kth largest in ascending sort order

    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[store_index], nums[right] = nums[right], nums[store_index]
        return store_index

    left, right = 0, len(nums) - 1
    while left < right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        if pivot_index == target_index:
            break
        elif pivot_index < target_index:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

    return nums[target_index]


def find_kth_largest_heap(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(find_kth_largest_quickselect(nums, k))  # 5
    print(find_kth_largest_heap(nums, k))  # 5
