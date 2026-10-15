"""
Find the Starting Node of a Cycle - Floyd's Algorithm, Phase 2   (Difficulty: Medium)
Asked at: Amazon, Adobe

Problem:
Given the head of a singly linked list that may contain a cycle, return the node where
the cycle begins. If the list has no cycle, return None. Solve it in O(n) time using
O(1) extra space - no visited-node hash set.

Example:
    Input: 3 -> 2 -> 0 -> -4 -> (back to the node with value 2)
    Output: the node with value 2

    3 -> 2 -> 0 -> -4
         ^____________|
         (cycle starts here)

Approach:
- Phase 1: run slow/fast pointers (slow +1, fast +2) until they meet somewhere
  inside the cycle. If fast falls off the end (None), there is no cycle.
- Phase 2: the distance from the head to the cycle's start is equal to the
  distance from the meeting point to the cycle's start, measured going forward
  around the loop - this drops out of the algebra on how far slow and fast
  each travel before they meet.
- So restart one pointer at head and leave the other at the meeting point, then
  advance both one step at a time; the node where they meet is the cycle start.
- Edge cases: no cycle at all (return None), and a cycle whose start is the head
  itself (the phase-2 loop still finds it correctly).

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

    def create_cycle(self, target_node):
        if self.head is None:
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = target_node

    def detect_cycle_start(self):
        slow = self.head
        fast = self.head

        # Phase 1: Detect whether a cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            # No cycle found
            return None

        # Phase 2: Find the starting node of the cycle
        pointer1 = self.head
        pointer2 = slow

        while pointer1 is not pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1


# Example usage
ll = LL()

n1 = ll.insert(3)
n2 = ll.insert(2)
n3 = ll.insert(0)
n4 = ll.insert(-4)

# Create a cycle: -4 -> 2
ll.create_cycle(n2)

cycle_start = ll.detect_cycle_start()

if cycle_start:
    print("Cycle starts at:", cycle_start.data)
else:
    print("No cycle detected")


# Test a linked list without a cycle
ll2 = LL()
ll2.insert(1)
ll2.insert(2)

cycle_start = ll2.detect_cycle_start()

if cycle_start:
    print("Cycle starts at:", cycle_start.data)
else:
    print("No cycle detected")
