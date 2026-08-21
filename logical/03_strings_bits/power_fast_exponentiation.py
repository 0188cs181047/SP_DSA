"""
Power of a Number (Fast Exponentiation) - Binary Exponentiation   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
Given a base x and a non-negative integer exponent n, compute x raised to
the power n (x^n) without simply multiplying x by itself n times.

Example:
    Input: x = 2, n = 10
    Output: 1024

Approach:
- Instead of multiplying x by itself n times (O(n)), split the problem in
  half: x^n = (x^(n // 2))^2, with one extra factor of x tacked on when n
  is odd. This is the classic "divide and conquer" trick for exponents.
- Recursive version: compute half = power(x, n // 2), then return
  half * half (and multiply by x once more if n is odd).
- Iterative version: walk through the bits of n from least significant to
  most significant, squaring a running "current power" of x each step,
  and multiplying it into the result only when the current bit is set.
- Edge cases: n = 0 should return 1 for any x (including x = 0, by the
  usual convention that 0^0 = 1 here); negative n isn't handled since the
  problem assumes a non-negative exponent.

Time Complexity:  O(log n)
Space Complexity: O(log n) for the recursive version (call stack), O(1) for the iterative version
"""


def power_recursive(x, n):
    if n == 0:
        return 1

    half = power_recursive(x, n // 2)
    result = half * half
    if n % 2 == 1:
        result *= x
    return result


def power_iterative(x, n):
    result = 1
    current = x
    while n > 0:
        if n % 2 == 1:
            result *= current
        current *= current
        n //= 2
    return result


if __name__ == "__main__":
    x, n = 2, 10
    print(f"{x}^{n} (recursive):", power_recursive(x, n))
    print(f"{x}^{n} (iterative):", power_iterative(x, n))

    x, n = 3, 0
    print(f"{x}^{n} (recursive):", power_recursive(x, n))
    print(f"{x}^{n} (iterative):", power_iterative(x, n))
