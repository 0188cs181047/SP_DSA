"""
Maximum Product Subarray - Kadane Variant (track max & min)   (Difficulty: Medium)
Asked at: Amazon, Meta

Problem:
Given an array of integers (which may include negative numbers and zeros),
find the contiguous subarray (containing at least one number) which has the
largest product, and return that product.

Example:
    Input: [2, 3, -2, 4]
    Output: 6   (subarray [2, 3])

Approach:
- Unlike sum, product is not monotonic under sign changes: multiplying a
  running max by a negative number can turn it into the new running min,
  and vice versa. So at each index track both a running max product and a
  running min product ending at that index.
- If the current number is negative, swap the running max and min before
  updating them, since the negative number is about to invert their roles.
- At each step, the new max/min is either the number itself (starting a
  fresh subarray) or the number times the previous max/min.
- Edge cases: a zero resets both running products to 0 naturally (since
  num=0 dominates num * prod when prod is non-positive... more precisely,
  max(0, prod*0) = max(0, 0) = 0), which correctly breaks the subarray
  there. A single-element array just returns that element.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def max_product_subarray(nums):
    result = nums[0]
    max_prod = nums[0]
    min_prod = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        result = max(result, max_prod)

    return result


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(max_product_subarray(nums))  # 6
