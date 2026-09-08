"""
Sum All Positive Numbers in a Nested Dictionary
(Difficulty: Easy-Medium)
Asked at: TCS, Infosys, Wipro, Accenture, Capgemini

Problem:
Given a nested dictionary containing integers and other dictionaries,
find the sum of all positive integers.

Ignore:
- Negative numbers
- Zero
- Non-integer values

Example:
    Input:
        {
            "k1": 12,
            "k2": {"k3": -1},
            "k4": {"k5": {"k6": 0}},
            "k7": 4
        }

    Output:
        16

Explanation:
    Positive numbers:
        12 + 4 = 16

Approach:
- Traverse each key-value pair in the dictionary.
- If the value is an integer and greater than 0,
  add it to the total sum.
- If the value is another dictionary,
  recursively process it.
- Return the final sum.

Time Complexity: O(n)

Space Complexity: O(d)

Where:
    n = Total number of elements
    d = Maximum depth of nesting
"""

def sum_positive_number(value):
    total = 0

    for key, val in value.items():

        # Check for positive integer
        if isinstance(val, int):
            if val > 0:
                total += val

        # Recursive call for nested dictionary
        elif isinstance(val, dict):
            total += sum_positive_number(val)

    return total


if __name__ == "__main__":

    value = {
        "k1": 12,
        "k2": {"k3": -1},
        "k4": {"k5": {"k6": 0}},
        "k7": 4
    }

    res = sum_positive_number(value)

    print(res)