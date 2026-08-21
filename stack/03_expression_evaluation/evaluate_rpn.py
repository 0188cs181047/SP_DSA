"""
Evaluate Reverse Polish Notation - Stack-based Evaluation   (Difficulty: Medium)
Asked at: Amazon, LinkedIn, Google

Problem:
Evaluate an arithmetic expression given as a list of tokens in Reverse Polish
Notation (postfix notation). Valid tokens are integers (which may be
negative) and the operators +, -, *, and /. Division between two integers
should truncate toward zero. Assume the expression is always valid.

Example:
    Input:  ["2", "1", "+", "3", "*"]
    Output: 9   (because (2 + 1) * 3 = 9)

    Input:  ["4", "13", "5", "/", "+"]
    Output: 6   (because 4 + (13 / 5) = 4 + 2 = 6)

Approach:
- Scan the tokens left to right, pushing every operand onto a stack.
- When an operator is seen, pop the top two operands off the stack - the
  second-popped value is the left operand, the first-popped is the right
  operand - apply the operator, and push the result back onto the stack.
- Because RPN removes the need for parentheses or precedence rules, a
  single left-to-right pass with a stack is enough; whatever remains on
  the stack at the end is the answer.
- Edge cases: negative operand tokens (e.g. "-3") must not be confused with
  the "-" operator token, and integer division must truncate toward zero
  rather than floor (matters for negative results, e.g. -7 / 2 == -3, not
  -4).

Time Complexity:  O(n), one pass over the tokens with O(1) stack work each
Space Complexity: O(n), for the operand stack
"""


def eval_rpn(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(int(left / right))  # truncate toward zero
        else:
            stack.append(int(token))

    return stack[0]


if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    print(f"Input:  {tokens}")
    print(f"Output: {eval_rpn(tokens)}")

    tokens = ["4", "13", "5", "/", "+"]
    print(f"Input:  {tokens}")
    print(f"Output: {eval_rpn(tokens)}")
