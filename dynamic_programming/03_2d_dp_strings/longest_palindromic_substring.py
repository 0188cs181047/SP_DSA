"""
Longest Palindromic Substring - Expand Around Center   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Meta

Problem:
Given a string s, find the longest substring of s that is a palindrome
(reads the same forwards and backwards). If several substrings share the
maximum length, returning any one of them is acceptable.

Example:
    Input: s = "babad"
    Output: "bab"   (or "aba" - both are valid longest palindromes)

Approach:
- Every palindrome mirrors around a center, which is either a single
  character (odd length, e.g. "aba") or the gap between two characters
  (even length, e.g. "abba").
- For every index i, expand outward from both possible centers - (i, i)
  for odd length and (i, i+1) for even length - as long as the characters
  on each side keep matching.
- Track the widest palindrome seen across all centers and slice it out at
  the end.
- Edge cases: an empty string returns "", and a single character is
  trivially its own longest palindrome.
- Alternative: a 2D DP where dp[i][j] is True when s[i:j+1] is a
  palindrome, using dp[i][j] = s[i] == s[j] and dp[i+1][j-1]. That is also
  O(n^2) time but needs O(n^2) space, whereas expanding around centers
  only needs O(1) extra space.

Time Complexity:  O(n^2) - n possible centers, each expansion up to O(n)
Space Complexity: O(1) extra space (excluding the returned substring)
"""


def longest_palindromic_substring(s):
    if not s:
        return ""

    start, end = 0, 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # the loop overshoots by one step on each side once it stops
        return left + 1, right - 1

    for i in range(len(s)):
        l1, r1 = expand(i, i)        # odd-length palindrome centered at i
        if r1 - l1 > end - start:
            start, end = l1, r1

        l2, r2 = expand(i, i + 1)    # even-length palindrome centered between i, i+1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


if __name__ == "__main__":
    s = "babad"
    print(f"s = '{s}'")
    print("Longest palindromic substring:", longest_palindromic_substring(s))
