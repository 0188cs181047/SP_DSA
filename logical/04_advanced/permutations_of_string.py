"""
Print All Permutations of a String - Backtracking (swap-based)   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Google

Problem:
Given a string of distinct characters, print (or return) every possible
permutation of its characters. Order of the output permutations doesn't
matter, but every rearrangement must appear exactly once.

Example:
    Input: s = "ABC"
    Output: ["ABC", "ACB", "BAC", "BCA", "CBA", "CAB"]

Approach:
- Think of the string as a list of characters. At each recursive level,
  pick a position `start` and try every character from `start` to the end
  as the one that goes into that position, by swapping it into place.
- Swap characters[start] with characters[i], recurse on start + 1 to fix
  the next position, then swap back before trying the next i. Swapping
  back (backtracking) restores the array so the next candidate at this
  level sees the original ordering, not one mutated by a previous choice.
- Base case: when start reaches the end of the list, the whole list is one
  completed permutation - join it into a string and record it.
- This in-place swap approach avoids building extra "remaining characters"
  strings at each level, so it only needs O(n) extra space for the
  recursion stack instead of O(n) per call for slicing.
- Edge cases: empty string produces one permutation (the empty string
  itself); repeated characters will produce duplicate permutations unless
  explicitly deduplicated (not required by this problem's distinct-chars
  assumption).

Time Complexity:  O(n * n!) - there are n! permutations, each takes O(n) to build/join
Space Complexity: O(n) for the recursion stack (plus O(n * n!) to store all results)
"""


def permutations_of_string(s):
    chars = list(s)
    n = len(chars)
    result = []

    def backtrack(start):
        if start == n:
            result.append("".join(chars))
            return

        for i in range(start, n):
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]

    backtrack(0)
    return result


if __name__ == "__main__":
    s = "ABC"
    perms = permutations_of_string(s)
    print(f"Permutations of '{s}':", perms)
    print("Count:", len(perms))
