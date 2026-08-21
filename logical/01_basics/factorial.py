"""
Factorial of a Number (Iterative & Recursive) - Iteration / Recursion   (Difficulty: Easy)
Asked at: TCS, Infosys, Amazon

Problem:
Given a non-negative integer n, compute n! (the product of all positive
integers from 1 to n). By definition, 0! = 1.

Example:
    Input: n = 5
    Output: 120

Approach:
- Iterative: multiply a running product by each integer from 1 to n in a
  simple loop. Uses O(1) extra space.
- Recursive: n! = n * (n-1)! with the base case 0! = 1. Clean to write but
  costs O(n) call-stack space and risks hitting Python's recursion limit
  for very large n, so the iterative version is preferred in practice.
- Edge case: n = 0 should return 1, not 0.

Time Complexity:  O(n) for both versions
Space Complexity: O(1) iterative, O(n) recursive (call stack)
"""


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    n = 5
    print("n =", n)
    print("Iterative:", factorial_iterative(n))
    print("Recursive:", factorial_recursive(n))
