"""
Reverse an Integer Without Using str()
(Difficulty: Easy)
Asked at: TCS, Infosys, Wipro, Accenture, Capgemini

Problem:
Given an integer n, reverse its digits without converting the integer
into a string.

Example:
    Input:  n = 12345
    Output: 54321

Another Example:
    Input:  n = 1200
    Output: 21

Approach:
- Use the modulo operator (%) to extract the last digit of the number.
- Add the extracted digit to the reversed number.
- Use integer division (//) to remove the last digit from the original number.
- Continue until the original number becomes 0.
- Handle negative numbers separately by storing the sign.

Example for n = 1234:

    Step 1:
        digit = 1234 % 10 = 4
        reverse = 0 * 10 + 4 = 4
        n = 1234 // 10 = 123

    Step 2:
        digit = 123 % 10 = 3
        reverse = 4 * 10 + 3 = 43
        n = 123 // 10 = 12

    Step 3:
        digit = 12 % 10 = 2
        reverse = 43 * 10 + 2 = 432
        n = 12 // 10 = 1

    Step 4:
        digit = 1 % 10 = 1
        reverse = 432 * 10 + 1 = 4321
        n = 1 // 10 = 0

    Final Output:
        4321

Time Complexity: O(log10(n))

Space Complexity: O(1)
"""


def reverse_integer(num):
    sign = -1 if num < 0 else 1
    num = abs(num)

    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return sign * reverse


if __name__ == "__main__":
    num = 12345

    res = reverse_integer(num)

    print(res)