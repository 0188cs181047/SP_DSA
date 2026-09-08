"""
Check if a Number is Prime - Trial Division
(Difficulty: Easy)
Asked at: TCS, Infosys, Wipro, Accenture, Capgemini

Problem:
Given a positive integer n, determine whether a number is prime.
A prime number is a number greater than 1 that has exactly two factors:
1 and itself.

Example:
    Input: n = 20
    Output: [2, 3, 5, 7, 11, 13, 17, 19]

Approach:
- Numbers less than 2 are not prime, so return False.
- Start checking divisibility from 2.
- If n is divisible by any number other than 1 and itself,
  then n is not prime.
- If no divisor is found, the number is prime.
- Generate all prime numbers from 0 to n-1 using a list comprehension.

Time Complexity:
    O(n * sqrt(n))  -- for generating all primes efficiently
    O(n)            -- for the result list

Space Complexity:
    O(n)

Note:
The current implementation checks divisors up to n/2, so its
prime-checking complexity is O(n). Therefore, for the exact code
provided, generating primes from 0 to n-1 has O(n²) worst-case time.

It can be optimized by checking divisors only up to sqrt(n).
"""

def prime_factor(val):
    if val < 2:
        return False

    for i in range(2, int(val/2) + 1):
        if val % i == 0:
            return False

    return True

if __name__ == "__main__":
    n = 20
    res = [val for val in range(n) if prime_factor(val)]
    print(res)
