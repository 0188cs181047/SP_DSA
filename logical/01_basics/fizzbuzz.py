"""
FizzBuzz - Modulo Check   (Difficulty: Easy)
Asked at: TCS, Infosys, Amazon, Wipro

Problem:
Print the numbers from 1 to n, but for multiples of 3 print "Fizz" instead
of the number, for multiples of 5 print "Buzz", and for multiples of both
3 and 5 print "FizzBuzz".

Example:
    Input: n = 15
    Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
              11, "Fizz", 13, 14, "FizzBuzz"]

Approach:
- Check divisibility by 15 (3 * 5) first since "divisible by both" is a
  stricter condition than either individual check.
- Fall back to checking 3 alone, then 5 alone, then the number itself.
- Order of checks matters: checking 3 or 5 before 15 would print "Fizz"
  or "Buzz" for a number that should print "FizzBuzz".

Time Complexity:  O(n)
Space Complexity: O(n) for the returned list, O(1) if just printing
"""


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    n = 15
    output = fizzbuzz(n)
    print("n =", n)
    print("Output:", output)
