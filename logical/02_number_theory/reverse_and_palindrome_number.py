"""
Reverse a Number & Check Palindrome Number - Digit Extraction (% and //)   (Difficulty: Easy)
Asked at: TCS, Wipro, Amazon

Problem:
Given an integer n, reverse its digits to produce a new number, and
separately determine whether n reads the same forwards and backwards
(a palindrome number). Both problems share the same digit-extraction
technique.

Example:
    Input: n = 1234
    Output: reverse = 4321, is_palindrome = False

Approach:
- Repeatedly pull off the last digit with n % 10, then build the reversed
  number as reversed_num = reversed_num * 10 + digit, and strip the digit
  off n with n //= 10.
- A number is a palindrome exactly when it equals its own reverse, so the
  palindrome check just calls the reverse function and compares.
- Edge cases: negative numbers are never palindromes (the sign flips the
  comparison); numbers ending in 0 lose those trailing zeros once reversed
  (e.g. reverse(120) = 21), which is expected for numeric reversal.

Time Complexity:  O(d) where d is the number of digits in n
Space Complexity: O(1)
"""


def reverse_number(n):
    negative = n < 0
    n = abs(n)

    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return -reversed_num if negative else reversed_num


def is_palindrome_number(n):
    if n < 0:
        return False
    return n == reverse_number(n)


if __name__ == "__main__":
    n = 1234
    print("n =", n)
    print("Reversed:", reverse_number(n))
    print("Is palindrome:", is_palindrome_number(n))

    n = 1221
    print("n =", n)
    print("Reversed:", reverse_number(n))
    print("Is palindrome:", is_palindrome_number(n))
