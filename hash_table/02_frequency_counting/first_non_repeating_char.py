"""
First Non-Repeating Character in a String - HashMap Frequency Count   (Difficulty: Easy)
Asked at: Amazon, Microsoft, TCS, Infosys

Problem:
Given a string s, find the first character that does not repeat anywhere
else in the string and return it. If every character repeats, return an
empty string (or None).

Example:
    Input: s = "swiss"
    Output: "w"   ('s' and 'i' repeat, 'w' is the first character seen only once)

Approach:
- First pass: count how many times every character occurs using a dict
  (or collections.Counter) - this only needs the character, not its
  position.
- Second pass: walk the string in its original order and return the
  first character whose count is exactly 1 - this pass is what
  guarantees the result is the *first* non-repeating character, since
  a dict alone has no notion of original order.
- Two linear passes beat checking each character against the rest of
  the string (which would be O(n^2)).
- Edge case: if no character has a count of 1 (every character repeats,
  including the empty-string case), return "" to signal "none found".

Time Complexity:  O(n)
Space Complexity: O(1) extra (at most 26 lowercase letters / a fixed alphabet size)
"""

from collections import Counter


def first_non_repeating_char(s):
    freq = Counter(s)

    for ch in s:
        if freq[ch] == 1:
            return ch

    return ""


if __name__ == "__main__":
    s = "swiss"
    print(f"String: '{s}'")
    print("First non-repeating character:", repr(first_non_repeating_char(s)))

    s2 = "aabbcc"
    print(f"\nString: '{s2}'")
    print("First non-repeating character:", repr(first_non_repeating_char(s2)))
