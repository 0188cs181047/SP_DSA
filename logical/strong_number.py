"""
Check Whether a Number is a Strong Number
(Difficulty: Easy)
Asked at: TCS, Infosys, Wipro, Accenture, Capgemini

Problem:
Given a positive integer, determine whether it is a Strong Number.

A Strong Number is a number where the sum of the factorials of each
individual digit is equal to the original number.

Example:
    Input:  n = 145

    Calculation:
        1! + 4! + 5!
        = 1 + 24 + 120
        = 145

    Output:
        True

Another Example:
    Input:  n = 123

    Calculation:
        1! + 2! + 3!
        = 1 + 2 + 6
        = 9

    Since 9 != 123:
        Output: False

Approach:
- Create a factorial function to calculate the factorial of a number.
- Extract each digit from the input number.
- Calculate the factorial of each digit.
- Add all the factorial values.
- Compare the calculated sum with the original number.
- If both are equal, the number is a Strong Number.

Time Complexity: O(d * k)

Space Complexity: O(1)

Where:
    d = number of digits in the input number
    k = maximum digit value (9)

Since factorial is calculated only for digits from 0 to 9,
the factorial calculation can be considered constant time.
Therefore, the overall complexity is effectively O(d).
"""


def factorial(val):
    factorial_value = 1

    for v in range(1, val + 1):
        factorial_value *= v

    return factorial_value


def strong_number(value):
    strong_sum = 0

    for digit in str(value):
        strong_sum += factorial(int(digit))

    return value == strong_sum


if __name__ == "__main__":
    n = 145

    res = strong_number(value=n)

    print(res)