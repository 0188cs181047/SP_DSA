"""
Reverse an Array In-Place - Two Pointers   (Difficulty: Easy)
Asked at: Amazon, Wipro, Accenture

Problem:
Given an array, reverse the order of its elements without using any extra array or
built-in reverse function, so the last element becomes the first and so on. The
reversal should happen in-place, modifying the original array directly.

Example:
    Input: [10, 20, 30, 40, 50]
    Output: [50, 40, 30, 20, 10]

    left -> [10, 20, 30, 40, 50] <- right
             swap 10 and 50
            [50, 20, 30, 40, 10]
                 swap 20 and 40
            [50, 40, 30, 20, 10]
                 left meets right, done

Approach:
- Keep two pointers, one starting at the front (left) and one at the back (right).
- Swap the elements at left and right, then move left forward and right backward.
- Stop once left and right meet or cross, since the whole array has been mirrored by then.
- No temporary array is needed, so the swap happens directly in the given array.
- Edge cases: an empty array or single-element array needs no swaps (pointers never cross),
  and an even-length array leaves no middle element untouched while an odd-length one has
  a middle element that stays put since it swaps with itself.

Time Complexity:  O(n) - each element is touched once across all the swaps
Space Complexity: O(1) - the array is reversed in-place with no auxiliary storage
"""


def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    print("Before:", nums)
    reverse_array(nums)
    print("After: ", nums)
