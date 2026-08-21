"""
Largest Number Formed From an Array of Numbers - Custom Comparator Sort   (Difficulty: Medium)
Asked at: Amazon, Google

Problem:
Given an array of non-negative integers, arrange them so that concatenating
them together (as strings) forms the largest possible number, and return
that number as a string. Regular numeric or lexicographic sort gives the
wrong order here - for example "9" and "34" sort as "34" < "9" numerically,
but "934" > "349" as a concatenation, so "9" must come first.

Example:
    Input:  [3, 30, 34, 5, 9]
    Output: "9534330"

Approach:
- Convert every number to a string first - the comparison that matters is
  which concatenation order (a+b vs b+a) produces the lexicographically
  larger string, not the numeric value of a or b on their own.
- Sort the strings with a custom comparator built via functools.cmp_to_key:
  for two candidates a and b, a should come before b if (a+b) > (b+a).
  This total order is exactly what "greedily pick the digit-prefix that
  wins" needs, and it composes correctly across the whole array.
- Edge case: if the array is all zeros (e.g. [0, 0]), the naive join gives
  "00" - detect a leading zero in the result and collapse it to a single "0".

Time Complexity:  O(n log n * k) - n log n comparisons, each comparing
                  strings of length up to k (the longest number's digit count)
Space Complexity: O(n * k) for the list of string representations
"""

from functools import cmp_to_key


def largest_number(nums):
    digits = [str(num) for num in nums]

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0

    digits.sort(key=cmp_to_key(compare))

    result = "".join(digits)
    return "0" if result[0] == "0" else result


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    print("Input: ", nums)
    print("Output:", largest_number(nums))

    zeros = [0, 0]
    print("Input: ", zeros)
    print("Output:", largest_number(zeros))
