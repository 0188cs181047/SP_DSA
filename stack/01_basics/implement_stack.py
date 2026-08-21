"""
Implement a Stack (Array-based & Linked-list-based) - Core Data Structure   (Difficulty: Easy)
Asked at: TCS, Infosys, Amazon

Problem:
Implement a stack data structure from scratch, supporting push, pop, peek,
and is_empty operations. A stack is Last-In-First-Out (LIFO): the last
element pushed is the first one popped. Implement it two ways - once backed
by a Python list, and once backed by a singly linked list of nodes - since
interviewers often ask for both to check you understand the underlying
trade-offs.

Example:
    Input: push(10), push(20), push(30), pop(), peek()
    Output: pop() -> 30, peek() -> 20   (30 was the last one in, so it's
            the first one out)

Flow diagram (array-based stack, top is the end of the list):
    push(10)      push(20)      push(30)       pop() -> 30
    [10]     ->   [10, 20]  ->  [10, 20, 30] -> [10, 20]
                                       ^top             ^top

Approach:
- Array-based stack: use a plain Python list and only ever touch its end
  (append/pop), so push/pop/peek are all O(1) amortized - no shifting of
  other elements is ever needed.
- Linked-list-based stack: keep a `top` pointer to a singly linked list of
  nodes. Pushing means creating a new node that points to the current top
  and making it the new top; popping means reading top's data and moving
  top to top.next. Both are O(1) since nothing but the head ever changes.
- Both versions raise an error on pop/peek from an empty stack rather than
  returning a sentinel, so callers can't silently mistake "empty" for a
  real value; is_empty() lets callers check before calling pop/peek.

Time Complexity:  O(1) for push, pop, peek, is_empty (both implementations)
Space Complexity: O(n) to hold n elements
"""


class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        popped = self.top
        self.top = self.top.next
        self._size -= 1
        return popped.value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size


if __name__ == "__main__":
    array_stack = ArrayStack()
    array_stack.push(10)
    array_stack.push(20)
    array_stack.push(30)
    print("Array-based stack:")
    print("  pop():", array_stack.pop())
    print("  peek():", array_stack.peek())
    print("  size():", array_stack.size())

    linked_stack = LinkedListStack()
    linked_stack.push(10)
    linked_stack.push(20)
    linked_stack.push(30)
    print("Linked-list-based stack:")
    print("  pop():", linked_stack.pop())
    print("  peek():", linked_stack.peek())
    print("  size():", linked_stack.size())
