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


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle_start(head):
    slow = head
    fast = head
    found_cycle = False

    # Phase 1: race slow and fast until they meet, or fast hits the end.
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            found_cycle = True
            break

    if not found_cycle:
        return None

    # Phase 2: one pointer from head, one from the meeting point, both step by step.
    pointer1 = head
    pointer2 = slow
    while pointer1 is not pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


if __name__ == "__main__":
    # Build 3 -> 2 -> 0 -> -4 -> back to node(2), forming a cycle.
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # creates the cycle, starting at n2

    start = detect_cycle_start(n1)
    print(start.val)  # 2

    # A plain list with no cycle.
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    print(detect_cycle_start(a))  # None
