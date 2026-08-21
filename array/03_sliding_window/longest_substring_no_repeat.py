"""
Longest Substring Without Repeating Characters - Variable Sliding Window + HashSet   (Difficulty: Medium)
Asked at: Amazon, Meta, Bloomberg

Problem:
Given a string s, find the length of the longest substring that does
not contain any repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3   (the substring "abc")

Approach:
- Expand a window with a right pointer, one character at a time, and
  keep a dict mapping each character to the index it was last seen at.
- If the incoming character was already seen inside the current window
  (its last-seen index is >= left), jump the left pointer to just past
  that previous occurrence instead of shrinking one step at a time -
  this keeps the whole scan O(n) rather than O(n^2).
- After every expansion, update the last-seen index for the current
  character and compare the current window length (right - left + 1)
  against the best seen so far.
- Edge cases: empty string returns 0; a string with all unique
  characters returns len(s).

Time Complexity:  O(n)
Space Complexity: O(min(n, charset size))
"""


def longest_substring_no_repeat(s):
    last_seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    s = "abcabcbb"
    print(f"String: {s!r}")
    print("Length of longest substring without repeating characters:",
          longest_substring_no_repeat(s))
