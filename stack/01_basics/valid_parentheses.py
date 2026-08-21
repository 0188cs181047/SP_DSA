"""
Valid Parentheses - Stack Matching   (Difficulty: Easy)
Asked at: Amazon, Google, Microsoft, Bloomberg

Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid. A string is valid if every
opening bracket has a matching closing bracket of the same type, and the
brackets close in the correct order (i.e. they're properly nested).

Example:
    Input: s = "{[()]}"
    Output: True

    Input: s = "([)]"
    Output: False

Approach:
- Push every opening bracket onto a stack as we scan left to right.
- On a closing bracket, the top of the stack must be its matching opening
  bracket - pop and compare; if the stack is empty or the top doesn't
  match, the string is invalid immediately.
- After scanning the whole string, it's only valid if the stack ended up
  empty (no unmatched opening brackets left dangling).
- Edge cases: an empty string is valid (nothing to mismatch); a string
  that starts with a closing bracket is caught by checking the stack isn't
  empty before popping; odd-length strings with only opening or only
  closing brackets are naturally rejected by the same two checks.

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    print(is_valid("{[()]}"))
    print(is_valid("([)]"))
