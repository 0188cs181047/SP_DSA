"""
Reverse a String Except Vowels
(Difficulty: Easy-Medium)
Asked at: TCS, Infosys, Wipro, Accenture, Capgemini

Problem:
Given a string, reverse all consonant characters while keeping vowels
at their original positions.

Vowels are:
    a, e, i, o, u
    A, E, I, O, U

Example:
    Input:  "hello"
    Output: "holle"

Explanation:
    Original:  h e l l o
    Vowels:      e     o
    Consonants: h l l

    Reverse consonants:
        l l h

    Result:
        h o l l e

Another Example:
    Input:  "python"
    Output: "nohtyp"

Approach:
- Convert the string into a list because strings are immutable in Python.
- Use two pointers:
    - left starts from the beginning.
    - right starts from the end.
- If the left character is a vowel, move left forward.
- If the right character is a vowel, move right backward.
- When both pointers point to consonants, swap them.
- Continue until left and right cross each other.
- Convert the list back into a string.

Time Complexity: O(n)

Space Complexity: O(n)

Where n is the length of the input string.
"""


def reverse_except_vowels(string):
    vowels = "aeiouAEIOU"

    chars = list(string)

    left = 0
    right = len(chars) - 1

    while left < right:

        # Skip vowels from the left
        if chars[left] in vowels:
            left += 1
            continue

        # Skip vowels from the right
        if chars[right] in vowels:
            right -= 1
            continue

        # Swap consonants
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)


if __name__ == "__main__":
    string = "hello"

    res = reverse_except_vowels(string)

    print(res)