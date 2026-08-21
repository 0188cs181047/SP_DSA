"""
Word Break - 1D DP + HashSet Dictionary   (Difficulty: Medium)
Asked at: Amazon, Google, Meta

Problem:
Given a string s and a list of words wordDict, determine whether s can be
segmented into a space-separated sequence of one or more dictionary words.
The same word from the dictionary may be reused any number of times.

Example:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: True   ("leet" + "code")

Approach:
- dp[i] means "the prefix s[0:i] can be fully segmented using words from
  the dictionary". dp[0] = True is the base case - the empty prefix needs
  no words at all.
- For every end index i, look back at every split point j < i: if dp[j] is
  already True and the piece s[j:i] is a word in the dictionary, then the
  whole prefix s[0:i] is also segmentable, so dp[i] = True.
- Store wordDict as a set first so each substring lookup is O(1) instead
  of scanning the list every time.
- Once dp[i] is confirmed True there is no need to keep checking other
  split points for that i - break out early.
- Edge cases: s that is itself one dictionary word, a dictionary that
  can't cover every leftover character (e.g. "catsandog" with
  ["cats","dog","sand","and","cat"] -> False), and an empty wordDict.

Time Complexity:  O(n^2) - n = len(s); for each end index we try every
                  earlier split point and slice/hash the substring
Space Complexity: O(n + W) - n for the dp array, W for the word set
"""


def word_break(s, word_dict):
    words = set(word_dict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]


if __name__ == "__main__":
    s = "leetcode"
    word_dict = ["leet", "code"]
    print(word_break(s, word_dict))  # True

    unsolvable_s = "catsandog"
    unsolvable_dict = ["cats", "dog", "sand", "and", "cat"]
    print(word_break(unsolvable_s, unsolvable_dict))  # False
