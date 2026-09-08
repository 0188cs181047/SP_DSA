"""
Reverse Each Word While Keeping Special Characters at the Same Index
(Difficulty: Easy-Medium)
Asked at: Accenture, TCS, Infosys, Wipro, Capgemini

Problem:
Given a string containing words, spaces, numbers, and special characters,
reverse only the alphabetic characters of each word while keeping every
special character at its original index.

Example:
    Input:  "Hello, World!"
    Output: "olleH, dlroW!"

Another Example:
    Input:  "Python@Developer!"
    Output: "nohtyP@repoleveD!"

Approach:
- Convert the string into a list so individual characters can be modified.
- Traverse the string character by character.
- Identify the beginning and ending position of each word.
- When a non-alphabetic character is found, reverse the alphabetic
  characters between the current word boundaries.
- Special characters such as ',', '!', '@', '?', spaces, etc. are not moved.
- Use two pointers (left and right) to reverse each word in-place.
- Finally, convert the character list back into a string.

Time Complexity:  O(n)
Space Complexity: O(n)

Where n is the length of the input string.
"""

def reverse_char(string):
    result = list(string)

    start = 0
    for i in range(len(string) + 1):
        if i == len(string) or not string[i].isalpha():
            left = start
            right = i - 1

            while left < right:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1

            start = i + 1

    return ''.join(result)


string = "Hello, World!"
res = reverse_char(string)

print(res)