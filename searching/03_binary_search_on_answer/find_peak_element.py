"""
Find Peak Element - Binary Search on the Slope   (Difficulty: Medium)
Asked at: Amazon, Google

Problem:
Given an integer array nums where no two adjacent elements are equal, find
the index of a peak element - an element that is strictly greater than its
neighbors. Elements at the boundary are compared only against their single
neighbor (treat out-of-bounds neighbors as negative infinity). If multiple
peaks exist, return the index of any one of them. Solve it faster than
O(n).

Example:
    Input:  nums = [1, 2, 3, 1]
    Output: 2   (nums[2] = 3 is greater than both neighbors)

    Input:  nums = [1, 2, 1, 3, 5, 6, 4]
    Output: 1 or 5   (both index 1 and index 5 are valid peaks)

Approach:
- A peak is guaranteed to exist for any such array (the array boundaries
  act like -infinity, so climbing "uphill" must eventually top out
  somewhere), which means we can binary search on the slope instead of
  scanning linearly.
- Compare nums[mid] with its right neighbor nums[mid + 1]. If nums[mid] <
  nums[mid + 1], the array is still rising, so a peak must lie somewhere
  to the right (mid itself cannot be the peak) - move low = mid + 1.
  Otherwise the array is falling (or mid is itself a peak), so a peak must
  lie at mid or to its left - move high = mid.
- This invariant always keeps at least one peak inside [low, high], so the
  loop converges to a single index which is guaranteed to be a peak.
- Edge cases: a single-element array is trivially its own peak; a strictly
  increasing or decreasing array converges to the last or first index
  respectively.

Time Complexity:  O(log n) - binary search halves the search space each step
Space Complexity: O(1) - only pointers are used
"""


def find_peak_element(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print("Input:", nums)
    print("Peak index:", find_peak_element(nums))

    nums = [1, 2, 1, 3, 5, 6, 4]
    print("Input:", nums)
    print("Peak index:", find_peak_element(nums))
