"""
Edit Distance (Levenshtein Distance) - 2D DP   (Difficulty: Hard)
Asked at: Google, Amazon, Microsoft

Problem:
Given two strings, word1 and word2, find the minimum number of operations
required to convert word1 into word2. You may insert a character, delete
a character, or replace a character, and each operation costs 1.

Example:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: horse -> rorse (replace 'h' with 'r')
                 rorse -> rose  (delete 'r')
                 rose  -> ros   (delete 'e')

Approach:
- Define dp[i][j] as the edit distance between word1[:i] and word2[:j].
- If the last characters match, no operation is needed for them, so
  dp[i][j] = dp[i-1][j-1].
- Otherwise, take 1 plus the best of the three possible operations:
    insert:  dp[i][j-1]     (make word1[:i] match word2[:j-1], then insert)
    delete:  dp[i-1][j]     (delete word1[i-1])
    replace: dp[i-1][j-1]   (replace word1[i-1] with word2[j-1])
- Base cases: turning an empty string into a string of length k always
  takes k insertions (and vice versa for deletions), so dp[0][j] = j and
  dp[i][0] = i.

Time Complexity:  O(m * n), where m and n are the lengths of the two strings
Space Complexity: O(m * n) for the dp table (can be reduced to O(min(m, n))
                  by keeping only two rows)
"""


def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # insert
                    dp[i - 1][j],      # delete
                    dp[i - 1][j - 1],  # replace
                )

    return dp[m][n]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(f"word1 = '{word1}', word2 = '{word2}'")
    print("Minimum edit distance:", edit_distance(word1, word2))
