"""
Design a Circular Queue - Fixed Array + Modulo   (Difficulty: Easy)
Asked at: TCS, Amazon

Problem:
Design a circular queue of a fixed capacity backed by a plain array. It
should support enqueue(x), dequeue(), front(), rear(), is_empty(), and
is_full(), all in O(1). Unlike a normal array queue, a circular queue
reuses the freed-up slots at the front instead of wasting them, so it
never runs out of room just because the front has advanced.

Example:
    Input:  CircularQueue(3)
            enqueue(1), enqueue(2), enqueue(3)   -> queue full: [1, 2, 3]
            dequeue()                            -> removes 1
            enqueue(4)                           -> reuses slot 0: [4, 2, 3]
    Output: front() -> 2, rear() -> 4

    indices:   0    1    2
    buffer:  [ 4 ,  2 ,  3 ]
               ^rear      ^front
             (rear wrapped around to index 0 after the dequeue freed it)

Approach:
- Use a fixed-size list as the backing buffer plus a `front` index and a
  `size` counter; the rear slot is always computed as
  (front + size) % capacity, so no separate rear pointer needs to be
  kept in sync.
- Advancing either pointer is just `index = (index + 1) % capacity` -
  the modulo is what lets index 0 follow right after the last index,
  turning the array into a ring instead of a dead-ending line.
- Track `size` explicitly rather than trying to infer empty/full from
  front == rear alone - with only front/rear, an empty queue and a full
  queue can land on the exact same pair of indices, so a counter is the
  simplest way to tell them apart.
- Edge cases: enqueue on a full queue and dequeue/front/rear on an empty
  queue are both rejected up front via is_full()/is_empty() checks.

Time Complexity:  O(1) for enqueue, dequeue, front, rear, is_empty, is_full
Space Complexity: O(capacity) for the backing buffer
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.front_index = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("enqueue on a full queue")
        rear_index = (self.front_index + self.size) % self.capacity
        self.buffer[rear_index] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        value = self.buffer[self.front_index]
        self.front_index = (self.front_index + 1) % self.capacity
        self.size -= 1
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("front of an empty queue")
        return self.buffer[self.front_index]

    def rear(self):
        if self.is_empty():
            raise IndexError("rear of an empty queue")
        rear_index = (self.front_index + self.size - 1) % self.capacity
        return self.buffer[rear_index]


if __name__ == "__main__":
    queue = CircularQueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("is_full:", queue.is_full())     # True

    print("dequeue:", queue.dequeue())     # 1
    queue.enqueue(4)                       # reuses the freed slot

    print("front:", queue.front())         # 2
    print("rear:", queue.rear())           # 4

    print("dequeue:", queue.dequeue())     # 2
    print("dequeue:", queue.dequeue())     # 3
    print("dequeue:", queue.dequeue())     # 4
    print("is_empty:", queue.is_empty())   # True
