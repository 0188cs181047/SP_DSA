"""
Create a Chessboard Pattern Using 0 and 1
(Difficulty: Easy)
Asked at: TCS, Infosys, Wipro, Accenture, Capgemini

Problem:
Given an integer n, create an n x n chessboard pattern using "0" and "1".
The values should alternate in every row and column, similar to a
traditional chessboard pattern.

Example:
    Input: n = 4

    Output:
        ['0', '1', '0', '1']
        ['1', '0', '1', '0']
        ['0', '1', '0', '1']
        ['1', '0', '1', '0']

Approach:
- Create an empty list to store the complete chessboard.
- Use two nested loops:
    - The outer loop represents the rows.
    - The inner loop represents the columns.
- Use (i + j) % 2 to determine which value to place.
- If (i + j) is even, append "0".
- If (i + j) is odd, append "1".
- Add each completed row to the chessboard.
- Return the final n x n matrix.

Time Complexity: O(n²)

Space Complexity: O(n²)

Where n is the size of the chessboard.
"""


def create_cheshboard(val):
    cheshboared = []

    for i in range(val):
        inner_board = []

        for j in range(val):
            if (i + j) % 2 == 0:
                inner_board.append("0")
            else:
                inner_board.append("1")

        cheshboared.append(inner_board)

    return cheshboared


if __name__ == "__main__":
    val = 9

    res = create_cheshboard(val=val)

    for chesh in res:
        print(chesh)