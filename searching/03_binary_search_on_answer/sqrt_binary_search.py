"""
Square Root of a Number (Integer Sqrt) - Binary Search on the Answer   (Difficulty: Easy/Medium)
Asked at: Amazon, Microsoft

Problem:
Given a non-negative integer n, find the integer square root of n, i.e. the
largest integer x such that x*x <= n. You may not use the built-in sqrt
function (or any floating point math library). Return only the floor value.

Example:
    Input:  n = 8
    Output: 2   (since 2*2 = 4 <= 8 but 3*3 = 9 > 8)

Approach:
- The function x -> x*x is monotonically increasing for x >= 0, so the set
  of values of x satisfying x*x <= n forms a contiguous prefix of
  [0, 1, ..., n]. That monotonic "yes/no" boundary is exactly what makes
  binary search on the answer applicable, even though we are searching over
  possible answers rather than over the input array itself.
- Binary search x in the range [0, n]. At each step, check the candidate
  mid: if mid*mid <= n, mid is a valid answer, so record it and try to push
  higher (search the right half); otherwise mid is too big, so search the
  left half.
- Edge cases: n = 0 and n = 1 both return themselves immediately since
  0*0 = 0 and 1*1 = 1; the search range naturally handles this without a
  special case.

Time Complexity:  O(log n) - binary search halves the range each step
Space Complexity: O(1) - only a few integer variables are used
"""


def sqrt_binary_search(n):
    if n < 2:
        return n

    low, high = 1, n
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer


if __name__ == "__main__":
    for n in [0, 1, 8, 15, 16, 25, 99]:
        print(f"sqrt({n}) = {sqrt_binary_search(n)}")
