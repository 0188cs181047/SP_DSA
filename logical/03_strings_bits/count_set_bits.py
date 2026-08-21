"""
Count Set Bits (1s) in an Integer - Bit Manipulation (Brian Kernighan's Algorithm)   (Difficulty: Easy/Medium)
Asked at: Amazon, Microsoft, Nvidia

Problem:
Given a non-negative integer n, count the number of set bits (1s) in its
binary representation. This is also known as the "population count" or
"Hamming weight" of the number.

Example:
    Input: n = 11   (binary: 1011)
    Output: 3

Approach:
- Brian Kernighan's trick: n & (n - 1) clears the lowest set bit of n.
  For example, if n = 1011 (11), then n - 1 = 1010, and 1011 & 1010 =
  1010, which zeroes out the rightmost 1 bit.
- Repeatedly apply this and count how many times it takes to bring n down
  to 0 - that count is exactly the number of set bits, and it only takes
  as many iterations as there are 1 bits (faster than checking every bit
  when the number is sparse).
- A simpler, equally valid alternative in Python is to lean on the
  built-in bin(n).count("1"), shown here for comparison.
- Edge case: n = 0 has zero set bits.

Time Complexity:  O(k) where k is the number of set bits (Brian Kernighan); O(log n) for the bin() approach
Space Complexity: O(1)
"""


def count_set_bits_kernighan(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def count_set_bits_builtin(n):
    return bin(n).count("1")


if __name__ == "__main__":
    n = 11
    print("n =", n, "(binary:", bin(n) + ")")
    print("Set bits (Kernighan):", count_set_bits_kernighan(n))
    print("Set bits (builtin):  ", count_set_bits_builtin(n))

    n = 0
    print("n =", n)
    print("Set bits (Kernighan):", count_set_bits_kernighan(n))
    print("Set bits (builtin):  ", count_set_bits_builtin(n))
