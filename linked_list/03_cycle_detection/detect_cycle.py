"""
Detect a Cycle in a Linked List (Floyd's Algorithm) - Slow/Fast Pointers   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Google

Problem:
Given the head of a singly linked list, determine whether the list contains a cycle -
a node that can be reached again by continuously following the "next" pointers. Return
True if a cycle exists, otherwise False. Solve it without modifying the list and
without using extra memory proportional to its length.

Example:
    Input: 3 -> 2 -> 0 -> -4 -> (back to the node with value 2)
    Output: True

    3 -> 2 -> 0 -> -4
         ^____________|

Approach:
- Use two pointers: slow moves one step at a time, fast moves two steps at a time.
- If the list has no cycle, fast reaches the end (None) before slow can catch up.
- If the list has a cycle, fast eventually laps slow from behind and they land on
  the exact same node - this is Floyd's Tortoise and Hare algorithm.
- Check fast and fast.next for None before advancing fast, so an odd-length or
  even-length tail never causes a crash.
- Edge cases: empty list and a single node pointing back to itself both need to
  fall through the loop guard correctly.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return node

        current = self.head

        while current.next:
            current = current.next

        current.next = node
        return node

    def create_cycle(self, targe_node):
        if self.head is None:
            return None

        current = self.head
        while current.next:
            current = current.next

        current.next = targe_node

    def detect_cycle(self):
      slow = self.head
      fast = self.head

      while fast is not None and fast.next is not None:
          slow = slow.next
          fast = fast.next.next

          if slow is fast:
              return True

      return False

ll = LL()
n1 = ll.insert(3)
n2 = ll.insert(2)
n3 = ll.insert(0)
n4 = ll.insert(-4)

ll.create_cycle(n2)

cycle_start = ll.detect_cycle()

if cycle_start:
    print("Yes cycle detected")
else:
    print("No cycle detected")


# Test a linked list without a cycle
ll2 = LL()
ll2.insert(1)
ll2.insert(2)

cycle_start = ll2.detect_cycle()

if cycle_start:
    print("Yes cycle detented")
else:
    print("No cycle detected")
