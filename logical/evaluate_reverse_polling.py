
def evalRPN(tokens):
    stack = []

    for token in tokens:

        # If the token is an operator
        if token in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)

            elif token == "*":
                stack.append(a * b)

            elif token == "/":
                # Truncate division toward zero
                result = abs(a) // abs(b)

                if (a < 0) != (b < 0):
                    result = -result

                stack.append(result)

        else:
            # Convert string to integer
            stack.append(int(token))

    return stack[-1]


tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))
