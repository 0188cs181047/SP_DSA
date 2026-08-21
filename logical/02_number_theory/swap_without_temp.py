"""
Swap Two Numbers Without a Temporary Variable - Arithmetic Trick / XOR Trick   (Difficulty: Easy)
Asked at: TCS, Wipro, Capgemini

Problem:
Given two variables a and b, swap their values without introducing a
third temporary variable to hold either value during the swap.

Example:
    Input: a = 5, b = 10
    Output: a = 10, b = 5

Approach:
- Arithmetic trick: a = a + b folds both values into a, then b = a - b
  recovers the original a, and a = a - b (using the new b) recovers the
  original b.
- XOR trick: a = a ^ b folds both values into a, then b = a ^ b recovers
  the original a (since x ^ y ^ y = x), and a = a ^ b recovers the
  original b the same way.
- Edge cases: the arithmetic version can silently overflow in fixed-width
  languages like C or Java; not a concern here since Python integers have
  arbitrary precision. Both tricks assume a and b are distinct variables,
  so "swapping" a value with itself is a trivial no-op either way.

Time Complexity:  O(1)
Space Complexity: O(1)
"""


def swap_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == "__main__":
    a, b = 5, 10
    print("Before:", a, b)
    print("Arithmetic swap:", swap_arithmetic(a, b))
    print("XOR swap:", swap_xor(a, b))
