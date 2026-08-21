"""
Remove the Nth Node From the End of a List - Fast/Slow Pointers with Offset   (Difficulty: Medium)
Asked at: Amazon, Meta

Problem:
Given the head of a singly linked list and an integer n, remove the nth node
from the end of the list and return the head of the resulting list. Do it in
a single pass over the list, without first counting its total length.

Example:
    Input:  head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5

Flow (n=2, fast starts n steps ahead of slow):
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    slow=dummy, fast=dummy, advance fast 2 steps -> fast=2
    move both together until fast hits the last node (5):
      slow=1 fast=3, slow=2 fast=4, slow=3 fast=5 (stop, fast.next is None)
    slow.next (=4) is the node to remove -> slow.next = slow.next.next

Approach:
- Use a dummy node before head so removing the actual head node (when n
  equals the list's length) doesn't need special-casing.
- Advance a fast pointer n steps ahead of a slow pointer first, then move
  both one step at a time until fast reaches the last node.
- At that point slow is sitting right before the node to delete, so
  slow.next = slow.next.next unlinks it in one pass.
- Edge cases: removing the head itself (n == length) is handled naturally
  because slow starts at the dummy node, not at head.

Time Complexity:  O(L), where L is the length of the list (single pass)
Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values) + " -> None")


def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    print("Original:")
    print_linked_list(head)

    result = remove_nth_from_end(head, 2)
    print("After removing 2nd from end:")
    print_linked_list(result)  # 1 -> 2 -> 3 -> 5 -> None
