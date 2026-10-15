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

    def print_ll(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head

        slow = dummy
        fast = dummy

        # Move fast pointer n steps forward
        for _ in range(n):
            if fast.next is None:
                raise ValueError("n is greater than the list length")
            fast = fast.next

        # Move both pointers until fast reaches the last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        # Update the linked list head
        self.head = dummy.next

    # Optional: return the head if you want to use the result
        return self.head


# Create linked list
ll = LL()

for value in [1, 2, 3, 4, 5]:
    ll.insert(value)

print("Original linked list:")
ll.print_ll()

ll.remove_nth_from_end(2)

print("After removing 2nd node from the end:")
ll.print_ll()