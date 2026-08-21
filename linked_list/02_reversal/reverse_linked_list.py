"""
Reverse a Linked List (Iterative & Recursive) - In-place Pointer Reversal   (Difficulty: Easy/Medium)
Asked at: Amazon, Microsoft, Google, TCS

Problem:
Given the head of a singly linked list, reverse the list in place and
return the new head. Do this without allocating a second list - only
pointers should move, not data.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
    Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

Flow (iterative, three pointers marching forward together):
    prev=None  curr=1->2->3->4->5
    step: prev=1  curr=2  (1 now points back to None)
    step: prev=2  curr=3  (2 now points back to 1)
    step: prev=3  curr=4  (3 now points back to 2)
    ...continues until curr is None, then prev is the new head.

Approach:
- Iterative: walk the list with prev/curr pointers. At each node, stash
  curr.next before overwriting it, point curr back at prev, then slide
  both pointers one step forward. When curr becomes None, prev is the
  new head.
- Recursive: recurse to the end of the list first, then on the way back
  up, flip each node's next pointer to point at its predecessor. The
  base case (empty list or single node) becomes the new head.
- Edge cases: empty list (head is None) and single-node list should both
  just return head unchanged, and both approaches naturally handle this
  since the loop/recursion doesn't touch anything in that case.
- Recursive version uses O(n) call-stack space, so prefer iterative for
  very long lists to avoid stack overflow.

Time Complexity:  O(n) for both versions
Space Complexity: O(1) iterative, O(n) recursive (call stack)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
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
        values.append(str(current.data))
        current = current.next
    print(" -> ".join(values) + " -> None")


def reverse_iterative(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def reverse_recursive(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    print("Original:")
    print_linked_list(head)

    reversed_head = reverse_iterative(head)
    print("Reversed (iterative):")
    print_linked_list(reversed_head)

    head_again = build_linked_list([1, 2, 3, 4, 5])
    reversed_head_recursive = reverse_recursive(head_again)
    print("Reversed (recursive):")
    print_linked_list(reversed_head_recursive)
