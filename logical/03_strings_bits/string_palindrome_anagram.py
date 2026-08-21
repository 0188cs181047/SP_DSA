"""
Check String Palindrome & Anagram of Two Strings - Two Pointers / Character Count   (Difficulty: Easy)
Asked at: TCS, Amazon, Microsoft

Problem:
Write two small string checks that come up constantly in interviews: (1)
determine whether a given string is a palindrome (reads the same forwards
and backwards), and (2) determine whether two given strings are anagrams
of each other (one can be rearranged into the other).

Example:
    Input: is_palindrome("madam")
    Output: True

    Input: is_anagram("listen", "silent")
    Output: True

Approach:
- Palindrome check: use two pointers starting at both ends of the string
  and move them inward, comparing characters at each step. If any pair
  mismatches, the string is not a palindrome.
- Anagram check: two strings are anagrams only if they have the same
  length and the same multiset of characters. Build a character-frequency
  count (a dict, or collections.Counter) for each string and compare them
  directly - this avoids the O(n log n) cost of sorting both strings.
- Edge cases: empty string is a palindrome by definition; strings of
  different lengths can never be anagrams, so bail out early on that check.

Time Complexity:  O(n) for both palindrome check and anagram check (character counting)
Space Complexity: O(1) for palindrome check, O(k) for anagram check (k = distinct characters)
"""

from collections import Counter


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


if __name__ == "__main__":
    word = "madam"
    print("String:", word)
    print("Is palindrome:", is_palindrome(word))

    word = "hello"
    print("String:", word)
    print("Is palindrome:", is_palindrome(word))

    s1, s2 = "listen", "silent"
    print("Strings:", s1, "and", s2)
    print("Is anagram:", is_anagram(s1, s2))

    s1, s2 = "hello", "world"
    print("Strings:", s1, "and", s2)
    print("Is anagram:", is_anagram(s1, s2))
