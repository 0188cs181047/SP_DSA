"""
Implement a Stack Using Queues - Single Queue Rotation Trick   (Difficulty: Easy/Medium)
Asked at: Amazon, Microsoft

Problem:
Implement a LIFO stack using only a queue (FIFO) as the underlying storage
- no other data structure allowed. Support push(x), which adds x to the
top, pop(), which removes and returns the most recently pushed element,
and top(), which peeks at it without removing it.

Example:
    Input:  push(1), push(2), push(3), pop(), top(), push(4), pop()
    Output: pop() -> 3, top() -> 2, pop() -> 4

    after push(1): [1]
    after push(2): [1, 2] -> rotate 1 element -> [2, 1]
    after push(3): [2, 1, 3] -> rotate 2 elements -> [3, 2, 1]
                                                       ^front is the newest push

Approach:
- Use a single queue. On every push, enqueue the new element at the back,
  then rotate the queue by dequeuing and re-enqueuing every element that
  was already there before this push (size - 1 of them).
- That rotation walks the newly-pushed element from the back all the way
  to the front, while the older elements slide behind it in their
  original relative order - so the front of the queue always holds the
  most recently pushed element, exactly what a stack's top needs to be.
- Because push does the reordering work, pop() and top() become trivial:
  just dequeue (or peek) the front of the queue in O(1).
- This trades push's cost (O(n) rotation) for O(1) pop/top - the mirror
  image of the classic "queue using two stacks" problem, where the
  expensive step happens on dequeue instead.
- Edge case: pop()/top() on an empty stack (assume valid usage here, as
  in a real interview).

Time Complexity:  O(n) for push, O(1) for pop and top
Space Complexity: O(n) to hold all pushed elements in the single queue
"""

from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, value):
        self.queue.append(value)
        # Rotate every element that existed before this push behind it,
        # so the just-pushed value ends up at the front.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.queue.popleft()

    def top(self):
        if self.is_empty():
            raise IndexError("top of an empty stack")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    stack = StackUsingQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("pop:", stack.pop())     # 3
    print("top:", stack.top())     # 2

    stack.push(4)
    print("pop:", stack.pop())     # 4
    print("pop:", stack.pop())     # 2
    print("pop:", stack.pop())     # 1
    print("is_empty:", stack.is_empty())   # True
