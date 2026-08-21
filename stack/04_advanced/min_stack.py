"""
Min Stack - Auxiliary Stack   (Difficulty: Medium)
Asked at: Amazon, Google, Meta

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum
element, all in O(1) time. Scanning the whole stack for the minimum on
every getMin() call would be O(n), which isn't good enough.

Example:
    Input:  push(5), push(3), push(7), getMin(), pop(), getMin()
    Output: getMin() -> 3, pop() removes 7, getMin() -> 3

    push(2)
    getMin() -> 2
    pop()
    getMin() -> 3

Approach:
- Keep a second stack that tracks the minimum seen so far, in lockstep
  with the main stack - one entry per push, never out of sync.
- On push(x), compare x to the current running minimum (or treat it as
  infinity if the stack is empty) and push the smaller value onto the
  min stack.
- On pop(), pop both stacks together, so the min stack's top always
  reflects the minimum of whatever remains on the main stack.
- Edge case: duplicate minimum values are handled naturally because the
  min stack stores one min per element, not a deduplicated set.

Time Complexity:  O(1) for push, pop, top, and get_min
Space Complexity: O(n) for the auxiliary min stack
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        current_min = min(value, self.min_stack[-1]) if self.min_stack else value
        self.min_stack.append(current_min)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(3)
    min_stack.push(7)
    print("getMin:", min_stack.get_min())  # 3

    print("pop:", min_stack.pop())         # 7
    print("getMin:", min_stack.get_min())  # 3

    min_stack.push(2)
    print("getMin:", min_stack.get_min())  # 2

    min_stack.pop()
    print("getMin after popping 2:", min_stack.get_min())  # 3
