"""
Isomorphic Strings - Two HashMaps (bidirectional mapping)   (Difficulty: Easy)
Asked at: Amazon, Google

Problem:
Given two strings s and t, determine if they are isomorphic. Two strings are
isomorphic if the characters in s can be replaced to get t, such that every
occurrence of a character maps to exactly one character in t, and no two
characters map to the same character (the mapping must be one-to-one in both
directions).

Example:
    Input: s = "egg", t = "add"
    Output: True

    Input: s = "foo", t = "bar"
    Output: False

Approach:
- Walk both strings in lockstep, building two hashmaps: s_char -> t_char and
  t_char -> s_char.
- At each position, if s[i] is already mapped, it must map to t[i]; if t[i]
  is already mapped, it must map back to s[i]. Either mismatch means the
  strings are not isomorphic.
- The reverse map is what catches cases like "ab" -> "aa", where a single
  s-char mapping would look consistent but two different s-chars collapse
  onto the same t-char.
- Different lengths can never be isomorphic; empty strings are trivially
  isomorphic.

Time Complexity:  O(n)
Space Complexity: O(k) where k is the number of distinct characters (bounded
                  by the alphabet size, so effectively O(1))
"""


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for s_char, t_char in zip(s, t):
        if s_char in s_to_t:
            if s_to_t[s_char] != t_char:
                return False
        else:
            s_to_t[s_char] = t_char

        if t_char in t_to_s:
            if t_to_s[t_char] != s_char:
                return False
        else:
            t_to_s[t_char] = s_char

    return True


if __name__ == "__main__":
    examples = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("ab", "aa"),
        ("badc", "baba"),
    ]

    for s, t in examples:
        print(f"s={s!r}, t={t!r} -> {is_isomorphic(s, t)}")
