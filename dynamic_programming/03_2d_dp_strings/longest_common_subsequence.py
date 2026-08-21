"""
Longest Common Subsequence (LCS) - 2D DP   (Difficulty: Medium)
Asked at: Amazon, Google, Microsoft

Problem:
Given two strings, text1 and text2, find the length of their longest
common subsequence - a sequence of characters that appears in both
strings in the same relative order, but not necessarily contiguously.
If the strings share no characters in common order, return 0.

Example:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3   (the LCS is "ace")

Approach:
- Define dp[i][j] as the LCS length of text1[:i] and text2[:j].
- If text1[i-1] == text2[j-1], the characters can be matched, so
  dp[i][j] = dp[i-1][j-1] + 1 (extend the subsequence diagonally).
- Otherwise, skip a character from one string or the other and keep the
  better result: dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
- Row 0 and column 0 stay 0 (an empty string has no common subsequence
  with anything), which anchors the recurrence.
- The actual subsequence, not just its length, can be recovered by
  walking the dp table backwards from dp[m][n].

Time Complexity:  O(m * n), where m and n are the lengths of the two strings
Space Complexity: O(m * n) for the dp table (can be reduced to O(min(m, n))
                  by keeping only two rows, since each cell only depends
                  on the previous row and the current row)
"""


def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def reconstruct_lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    chars = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            chars.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(chars))


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(f"text1 = '{text1}', text2 = '{text2}'")
    print("Length of LCS:", longest_common_subsequence(text1, text2))
    print("One valid LCS:", reconstruct_lcs(text1, text2))
