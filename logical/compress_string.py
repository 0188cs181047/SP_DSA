"""
Compress a String Using Run-Length Encoding (RLE)
(Difficulty: Easy-Medium)
Asked at: TCS, Infosys, Wipro, Accenture, Capgemini

Problem:
Given a string, compress consecutive repeated characters by replacing
each group of repeated characters with the character followed by the
number of times it occurs consecutively.

Example:
    Input:  "aaaabbbccaaa"
    Output: "a4b3c2a3"

Another Example:
    Input:  "aaabbc"
    Output: "a3b2c1"

Approach:
- Handle the None input case.
- Initialize an empty list to store the compressed result.
- Maintain a count variable to track consecutive occurrences.
- Start traversing the string from the second character.
- Compare the current character with the previous character.
- If both characters are the same, increment the count.
- If they are different:
    - Add the previous character and its count to the result.
    - Reset the count to 1 for the new character.
- After the loop, append the last character and its count.
- Join the result list to create the final compressed string.

Time Complexity: O(n)

Space Complexity: O(n)

Where n is the length of the input string.
"""


def compress_string(string_val):
    if string_val is None:
        return " "

    res_compress_str = []
    count = 1

    for i in range(1, len(string_val)):
        if string_val[i] == string_val[i - 1]:
            count += 1
        else:
            res_compress_str.append(f"{string_val[i - 1]}{count}")
            count = 1

    res_compress_str.append(f"{string_val[-1]}{count}")

    return "".join(res_compress_str)


if __name__ == "__main__":
    string_val = "aaaabbbccaaa"

    res = compress_string(string_val=string_val)

    print(res)