"""
GCD and LCM of Two Numbers - Euclidean Algorithm   (Difficulty: Easy)
Asked at: TCS, Infosys, Amazon

Problem:
Given two positive integers a and b, find their greatest common divisor
(GCD) - the largest number that divides both exactly - and their least
common multiple (LCM) - the smallest number that both divide exactly.

Example:
    Input: a = 24, b = 36
    Output: gcd = 12, lcm = 72

Approach:
- Euclid's insight: gcd(a, b) = gcd(b, a % b), because any common divisor
  of a and b also divides a % b. The recursion bottoms out at gcd(a, 0) = a.
- Once gcd is known, lcm falls out of the identity a * b = gcd(a, b) *
  lcm(a, b), so lcm(a, b) = abs(a * b) // gcd(a, b).
- Edge cases: gcd(a, 0) is a itself; the abs() in the lcm formula keeps
  the result sensible if a negative number is ever passed in.

Time Complexity:  O(log(min(a, b))) for gcd, same order for lcm
Space Complexity: O(log(min(a, b))) recursion stack for gcd, O(1) for lcm
"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = 24, 36
    print("a =", a, " b =", b)
    print("GCD:", gcd(a, b))
    print("LCM:", lcm(a, b))
