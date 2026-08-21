"""
Check if a Number is Prime - Trial Division up to sqrt(n)   (Difficulty: Easy)
Asked at: TCS, Infosys, Wipro

Problem:
Given a positive integer n, determine whether it is prime. A prime number
is greater than 1 and has no positive divisors other than 1 and itself.

Example:
    Input: n = 29
    Output: True

Approach:
- A number n cannot have a divisor greater than sqrt(n) without also having
  one smaller than sqrt(n), so it's enough to test divisors up to sqrt(n).
- Handle 2 as the only even prime, then only test odd divisors from 3
  upward, since checking even divisors beyond 2 is redundant.
- Edge cases: numbers less than 2 (0, 1, negatives) are not prime.

Time Complexity:  O(sqrt(n))
Space Complexity: O(1)
"""

import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    n = 29
    print("n =", n)
    print("Is prime:", is_prime(n))

    n = 30
    print("n =", n)
    print("Is prime:", is_prime(n))
