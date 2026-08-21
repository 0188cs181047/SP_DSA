"""
Roman Numeral to Integer and Integer to Roman - Greedy + Lookup Table   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Adobe

Problem:
Write two functions: one that converts an integer (1 to 3999) into its
Roman numeral representation, and one that converts a valid Roman numeral
string back into an integer.

Example:
    Input: integer_to_roman(1994)
    Output: "MCMXCIV"

    Input: roman_to_integer("MCMXCIV")
    Output: 1994

Approach:
- Integer -> Roman: keep a lookup table of (value, symbol) pairs sorted
  from largest to smallest, including the subtractive combinations
  (900 -> "CM", 400 -> "CD", 90 -> "XC", 40 -> "XL", 9 -> "IX", 4 -> "IV")
  alongside the plain ones (1000 -> "M", 500 -> "D", ...). Greedily take
  the largest pair whose value fits into what's left of n, append its
  symbol, subtract its value, and repeat until n reaches 0.
- Roman -> Integer: map each symbol to its value and scan left to right,
  adding a symbol's value to the running total, but subtracting it
  instead whenever it's smaller than the value of the symbol right after
  it (that's what makes "IV" read as 4 instead of 1 + 5 = 6).
- The subtractive-pair table for the integer -> Roman direction is the
  key trick: it turns the "irregular" cases (4, 9, 40, 90, 400, 900) into
  ordinary greedy lookups instead of special-cased string patches.
- Edge cases: this problem assumes valid input in the standard 1-3999
  range (Roman numerals don't have a standard way to write 0 or numbers
  requiring more than three consecutive "M"s).

Time Complexity:  O(1) for both directions - the numeral length is bounded by a small constant (at most ~15 symbols for values under 4000)
Space Complexity: O(1) - fixed-size lookup tables, aside from the output string
"""

INT_TO_ROMAN_TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
    (1, "I"),
]

ROMAN_TO_INT_TABLE = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000,
}


def integer_to_roman(n):
    result = []
    for value, symbol in INT_TO_ROMAN_TABLE:
        if n == 0:
            break
        count, n = divmod(n, value)
        result.append(symbol * count)
    return "".join(result)


def roman_to_integer(s):
    total = 0
    for i, ch in enumerate(s):
        value = ROMAN_TO_INT_TABLE[ch]
        if i + 1 < len(s) and value < ROMAN_TO_INT_TABLE[s[i + 1]]:
            total -= value
        else:
            total += value
    return total


if __name__ == "__main__":
    n = 1994
    roman = integer_to_roman(n)
    print(f"integer_to_roman({n}) =", roman)

    s = "MCMXCIV"
    number = roman_to_integer(s)
    print(f"roman_to_integer('{s}') =", number)

    n = 58
    print(f"integer_to_roman({n}) =", integer_to_roman(n))
    print(f"roman_to_integer('{integer_to_roman(n)}') =", roman_to_integer(integer_to_roman(n)))
