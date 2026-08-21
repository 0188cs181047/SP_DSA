"""
Heap Sort - Max-Heap Extraction   (Difficulty: Medium)
Asked at: Google, Amazon, Bloomberg

Problem:
Given an array of integers, sort it in ascending order using heap sort:
build a max-heap out of the array in place, then repeatedly pull the
largest remaining element out to the end of the array.

Example:
    Input:  [4, 10, 3, 5, 1]
    Output: [1, 3, 4, 5, 10]

    Array viewed as a binary heap (index i has children 2i+1, 2i+2):
                4
              /   \
            10      3
           /  \
          5    1

Approach:
- Build a max-heap in place: starting from the last non-leaf node and
  walking backward to the root, sift each node down so it (and everything
  below it) satisfies the max-heap property (parent >= both children).
- Repeatedly swap the root (the current maximum) with the last unsorted
  element, shrink the "heap" region by one, and sift the new root down -
  this peels off the largest remaining value into its final sorted spot
  each time, moving from the end of the array backward.
- Edge cases: empty/single-element array (no sifting needed). Everything
  happens in the original array (no extra array like merge sort needs),
  which is why heap sort gets O(n log n) time with only O(1) extra space.

Time Complexity:  O(n log n) - build-heap is O(n), then n extractions of O(log n)
Space Complexity: O(1) extra space (sorts in place)
"""


def heap_sort(arr):
    n = len(arr)

    # build max-heap: sift down every non-leaf node, bottom-up
    for root in range(n // 2 - 1, -1, -1):
        _sift_down(arr, root, n)

    # repeatedly move the current max to the end, then re-heapify the rest
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end)

    return arr


def _sift_down(arr, root, heap_size):
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left
        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest == root:
            break

        arr[root], arr[largest] = arr[largest], arr[root]
        root = largest


if __name__ == "__main__":
    nums = [4, 10, 3, 5, 1]
    print("Before:", nums)
    heap_sort(nums)
    print("After: ", nums)
