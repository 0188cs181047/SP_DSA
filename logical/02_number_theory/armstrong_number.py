"""
Check Armstrong Number - Digit Extraction + Power Sum   (Difficulty: Easy)
Asked at: TCS, Infosys

Problem:
Given a positive integer n, determine whether it is an Armstrong number
(also called a narcissistic number) - a number that equals the sum of
each of its own digits raised to the power of the total digit count.

Example:
    Input: n = 153
    Output: True   (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153)

Approach:
- First count how many digits n has, since that count is the exponent
  every digit gets raised to.
- Walk the digits again with the same % 10 / // 10 extraction, raising
  each digit to that power and accumulating the sum.
- Compare the accumulated sum against the original number.
- Edge cases: every single-digit number (0-9) is trivially an Armstrong
  number, since digit^1 always equals the digit itself.

Time Complexity:  O(d) where d is the number of digits in n
Space Complexity: O(1)
"""


def count_digits(n):
    count = 0
    temp = n
    while temp > 0:
        count += 1
        temp //= 10
    return count


def is_armstrong_number(n):
    digit_count = count_digits(n)

    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** digit_count
        temp //= 10

    return total == n


if __name__ == "__main__":
    n = 153
    print("n =", n)
    print("Is Armstrong number:", is_armstrong_number(n))

    n = 123
    print("n =", n)
    print("Is Armstrong number:", is_armstrong_number(n))
