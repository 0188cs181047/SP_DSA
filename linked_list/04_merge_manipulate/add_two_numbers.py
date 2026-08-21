"""
Add Two Numbers Represented as Linked Lists - Simulated Digit-by-Digit Addition + Carry   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Bloomberg

Problem:
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order (the head node holds the
least significant digit), and each node holds a single digit. Add the two
numbers and return the sum as a linked list, in the same reverse-digit format.

Example:
    Input:  l1 = 2 -> 4 -> 3 (represents 342),  l2 = 5 -> 6 -> 4 (represents 465)
    Output: 7 -> 0 -> 8 (represents 807)

Approach:
- Since digits are stored least-significant-first, adding the lists is just
  like adding two numbers on paper from right to left - walk both lists head
  to tail, no reversing needed.
- At each position, sum the two digits (treating a missing node as 0) plus
  any carry from the previous position; the new digit is total % 10 and the
  new carry is total // 10.
- Keep looping while either list still has nodes or a carry remains, so a
  trailing carry (e.g. 5 + 5 = 10) correctly appends one more node.
- Edge cases: lists of different lengths, and a final carry that extends the
  result by one extra digit beyond both input lists.

Time Complexity:  O(max(n, m)), where n and m are the lengths of the two lists
Space Complexity: O(max(n, m)) for the newly built result list
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


def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        tail.next = ListNode(total % 10)
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    return dummy.next


if __name__ == "__main__":
    l1 = build_linked_list([2, 4, 3])  # represents 342
    l2 = build_linked_list([5, 6, 4])  # represents 465

    print("L1:")
    print_linked_list(l1)
    print("L2:")
    print_linked_list(l2)

    result = add_two_numbers(l1, l2)
    print("Sum:")
    print_linked_list(result)  # 7 -> 0 -> 8 -> None (represents 807)
