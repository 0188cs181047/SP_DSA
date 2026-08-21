"""
Group Anagrams - HashMap keyed by sorted string / char-count   (Difficulty: Medium)
Asked at: Amazon, Meta, Microsoft, Uber

Problem:
Given an array of strings, group the strings that are anagrams of each
other into the same list. Two strings are anagrams if one can be formed
by rearranging the letters of the other. Return the groups in any order.

Example:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Approach:
- Any two anagrams produce the same string once their characters are
  sorted, so sorted(word) is a canonical signature shared by a whole
  anagram group - use it as a dict key and bucket every word under it.
- A dict naturally maps each signature to the list of original words
  that share it, so a single pass over the input builds every group.
- Sorting each word costs O(k log k) for a word of length k; an
  alternative is a 26-length character-count tuple as the key, which
  builds the signature in O(k) instead, trading a bit of clarity for
  speed on long words.
- Words that are already unique (no anagram partner) simply end up as
  a group of size one - no special casing needed.
- Order of the groups and order of words within a group is not
  specified by the problem, so no sorting of the output is required.

Time Complexity:  O(n * k log k), where n = number of words, k = max word length
Space Complexity: O(n * k)
"""

from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        signature = "".join(sorted(word))
        groups[signature].append(word)

    return list(groups.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {strs}")
    print("Grouped anagrams:", group_anagrams(strs))

    strs2 = ["", "a", ""]
    print(f"\nInput: {strs2}")
    print("Grouped anagrams:", group_anagrams(strs2))
