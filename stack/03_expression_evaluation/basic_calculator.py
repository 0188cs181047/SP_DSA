"""
Basic Calculator (+, -, parentheses) - Stack for Sign Context   (Difficulty: Hard)
Asked at: Google, Amazon, Microsoft

Problem:
Given a string containing digits, '+', '-', '(', ')', and spaces,
implement a basic calculator to evaluate it and return the result as an
integer. There is no multiplication or division, and the expression is
always valid (parentheses are balanced, numbers are non-negative literals
that may be preceded by unary +/- through the surrounding operators).

Example:
    Input:  "(1+(4+5+2)-3)+(6+8)"
    Output: 23

    Input:  " 2-1 + 2 "
    Output: 3

Approach:
- Walk the string once, building up multi-digit numbers digit by digit and
  tracking a running "sign" flag that gets set by the most recent + or -.
- Whenever a number is "closed off" (by hitting an operator, a closing
  paren, or the end of the string), fold sign * number into a running
  result and reset the number to 0.
- On '(', push the result and sign accumulated so far onto a stack, then
  reset result to 0 and sign to +1 so the parenthesized sub-expression is
  evaluated in its own fresh context.
- On ')', close off the sub-expression's number into its local result,
  then pop the saved sign and result and combine them: the sub-expression
  total gets multiplied by the sign that preceded the '(', then added to
  whatever result had accumulated before the '('.
- Edge cases: nested parentheses (the stack can grow arbitrarily deep),
  multi-digit numbers, leading unary minus (e.g. "-(1+2)"), and stray
  spaces anywhere in the string (simply ignored since they match none of
  the digit/operator/paren branches).

Time Complexity:  O(n), one pass over the string
Space Complexity: O(n), worst case stack depth for deeply nested parentheses
"""


def calculate(s):
    stack = []
    result = 0
    number = 0
    sign = 1

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == "+":
            result += sign * number
            number = 0
            sign = 1
        elif char == "-":
            result += sign * number
            number = 0
            sign = -1
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ")":
            result += sign * number
            number = 0
            result *= stack.pop()  # sign that preceded this '('
            result += stack.pop()  # result accumulated before this '('
        # spaces (and any other whitespace) are simply skipped

    result += sign * number
    return result


if __name__ == "__main__":
    expression = "(1+(4+5+2)-3)+(6+8)"
    print(f"Input:  {expression}")
    print(f"Output: {calculate(expression)}")

    expression = " 2-1 + 2 "
    print(f"Input:  {expression!r}")
    print(f"Output: {calculate(expression)}")
