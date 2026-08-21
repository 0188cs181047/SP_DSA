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


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


if __name__ == "__main__":
    # Build 3 -> 2 -> 0 -> -4 -> back to node(2), forming a cycle.
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # creates the cycle

    print(has_cycle(n1))  # True

    # A plain list with no cycle.
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    print(has_cycle(a))  # False
