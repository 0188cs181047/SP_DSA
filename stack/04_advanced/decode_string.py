"""
Decode String - Stack of (count, partial-string)   (Difficulty: Medium)
Asked at: Google, Amazon, Meta

Problem:
Given an encoded string in the form k[encoded_string], decode it so
that encoded_string is repeated exactly k times. k is always a positive
integer, and the encoding can nest arbitrarily deep (e.g. "3[a2[c]]").

Example:
    Input:  "3[a2[c]]"
    Output: "accaccacc"

    "3[a]2[bc]" -> "aaabcbc"

Approach:
- Walk the string one character at a time, building up the current
  digit (to support multi-digit counts like "10") and the current
  partial string.
- On '[', push the (string built so far, count so far) onto a stack,
  then reset both so the string inside the brackets starts fresh.
- On ']', pop the (previous_string, count) pair, repeat the
  just-finished inner string count times, and append it onto
  previous_string - that combined result becomes the new "current"
  string being built.
- Plain letters just get appended to the current string as they're read.
- Edge cases: multi-digit counts and brackets nested several levels
  deep, both of which the stack handles naturally via LIFO order.

Time Complexity:  O(n * maxk), where n is the input length and maxk is
                   the largest repeat count, since the decoded output
                   can be much longer than the input
Space Complexity: O(n) for the stack and the resulting decoded string
"""


def decode_string(s):
    stack = []
    current_string = ""
    current_count = 0

    for char in s:
        if char.isdigit():
            current_count = current_count * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_count))
            current_string = ""
            current_count = 0
        elif char == "]":
            previous_string, count = stack.pop()
            current_string = previous_string + current_string * count
        else:
            current_string += char

    return current_string


if __name__ == "__main__":
    example = "3[a2[c]]"
    print(f"{example} -> {decode_string(example)}")  # accaccacc

    example2 = "3[a]2[bc]"
    print(f"{example2} -> {decode_string(example2)}")  # aaabcbc
