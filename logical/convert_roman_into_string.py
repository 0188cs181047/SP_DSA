"""
Convert Roman Numerals to Integer
(Difficulty: Easy-Medium)
Asked at: TCS, Infosys, Wipro, Amazon, Microsoft, Google

Problem:
Given a string representing a Roman numeral, convert it into its
corresponding integer value.

Roman numeral symbols and their values:

    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

Example:
    Input:  "III"
    Output: 3

    Input:  "IV"
    Output: 4

    Input:  "IX"
    Output: 9

    Input:  "LVIII"
    Output: 58

    Input:  "MCMXCIV"
    Output: 1994

Approach:
- Store Roman numeral symbols and their integer values in a dictionary.
- Traverse the Roman numeral from left to right.
- If the current symbol has a smaller value than the next symbol,
  subtract the current value.
- Otherwise, add the current value.
- This handles subtractive combinations such as:
      IV = 4
      IX = 9
      XL = 40
      XC = 90
      CD = 400
      CM = 900
- Return the final sum.

Time Complexity: O(n)

Space Complexity: O(1)

Where n is the number of Roman numeral characters.
The dictionary contains only a fixed number of Roman symbols.
"""


def roman_to_number(roman):
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0

    for i in range(len(roman)):

        if i + 1 < len(roman) and roman_values[roman[i]] < roman_values[roman[i + 1]]:
            result -= roman_values[roman[i]]
        else:
            result += roman_values[roman[i]]

    return result


if __name__ == "__main__":
    roman = "IV"

    res = roman_to_number(roman)

    print(res)