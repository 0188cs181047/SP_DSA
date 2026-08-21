"""
Queue Using Two Stacks - Two Stacks   (Difficulty: Easy/Medium)
Asked at: Amazon, Microsoft

Problem:
Implement a FIFO queue using only two stacks (LIFO) as the underlying
storage - no other data structure allowed. Support enqueue(x), which
adds x to the back, and dequeue(), which removes and returns the
element that was enqueued first.

Example:
    Input:  enqueue(1), enqueue(2), enqueue(3), dequeue(), dequeue(), enqueue(4), dequeue()
    Output: 1, 2, 3  (in that order, matching FIFO order)

    stack_in after enqueues:  [1, 2, 3]  (3 on top)
    pour into stack_out:      [3, 2, 1]  (1 on top, ready to dequeue)

Approach:
- Push every enqueued element onto stack_in - that part is always O(1).
- On dequeue, if stack_out is empty, pour all of stack_in into
  stack_out (pop from one, push onto the other). That reverses the
  order so the oldest element ends up on top of stack_out.
- If stack_out still has elements from a previous pour, just pop from
  it directly - no need to touch stack_in until stack_out runs dry.
- This gives amortized O(1) per operation, even though a single
  dequeue can occasionally cost O(n) when it triggers a pour.
- Edge case: dequeuing from an empty queue (assume valid usage here,
  as in a real interview).

Time Complexity:  O(1) amortized for enqueue and dequeue
Space Complexity: O(n) to hold all queued elements across both stacks
"""


class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


if __name__ == "__main__":
    queue = QueueUsingStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("dequeue:", queue.dequeue())  # 1
    print("dequeue:", queue.dequeue())  # 2

    queue.enqueue(4)
    print("dequeue:", queue.dequeue())  # 3
    print("dequeue:", queue.dequeue())  # 4
