"""
Generate Binary Numbers from 1 to N - BFS-style String Generation   (Difficulty: Easy)
Asked at: Amazon

Problem:
Given a positive integer `n`, generate the binary representations of every
integer from 1 to n, in order, as strings (no leading zeros). Build them
by growing strings level by level rather than converting each number with
a built-in base-conversion call.

Example:
    Input:  n = 5
    Output: ["1", "10", "11", "100", "101"]

Approach:
- Notice that every binary string is formed by taking a shorter binary
  string and appending either "0" or "1" - "1" -> "10"/"11" -> "100"/
  "101"/"110"/"111", and so on. That parent/child relationship is exactly
  what a queue-driven BFS explores level by level.
- Seed the queue with "1" (the only 1-digit binary number with no leading
  zero). Repeatedly dequeue a string, record it as the next answer, then
  enqueue string + "0" and string + "1" as its children for later use.
- Stop as soon as n numbers have been recorded - the queue always has
  more candidates queued up than needed, so there's no risk of running
  out before hitting the count.
- Edge case: n = 1 just returns ["1"] after the very first dequeue.

Time Complexity:  O(n) - exactly n strings are dequeued and recorded
Space Complexity: O(n) - the queue and the result list each hold O(n) strings
"""

from collections import deque


def generate_binary_numbers(n):
    result = []
    queue = deque(["1"])

    while len(result) < n:
        binary = queue.popleft()
        result.append(binary)
        queue.append(binary + "0")
        queue.append(binary + "1")

    return result


if __name__ == "__main__":
    n = 5
    print("n:", n)
    print("binary numbers 1..n:", generate_binary_numbers(n))
    # ['1', '10', '11', '100', '101']
