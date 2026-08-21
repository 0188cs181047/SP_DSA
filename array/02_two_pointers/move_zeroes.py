"""
Move Zeroes to the End - Two Pointers   (Difficulty: Easy)
Asked at: Meta, Amazon, Bloomberg

Problem:
Given an array of integers, move all the zeroes to the end of the array while
maintaining the relative order of the non-zero elements. This must be done
in-place without making a copy of the array.

Example:
    Input: nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Approach:
- Keep a "write" pointer marking the next slot where a non-zero element
  belongs. Walk a "read" pointer across the array; whenever a non-zero value
  is found, swap it into the write slot and advance write.
- Swapping (rather than just overwriting) keeps everything in-place and
  naturally pushes zeroes toward the back as a side effect, without needing
  a separate pass to fill in zeroes at the end.
- Since write never moves past read, this is a single forward pass, O(n)
  time and O(1) extra space.
- Edge cases: an array of all zeroes or all non-zeroes should be left
  effectively unchanged (or fully unchanged), and a single-element array
  should short-circuit correctly since the loop just never swaps.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def move_zeroes(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(move_zeroes(nums))
