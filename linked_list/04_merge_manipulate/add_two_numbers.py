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
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    def print_ll(self, head=None):
        current = head if head else self.head

        if current is None:
            return

        while current:
            print(current.data, end="->")
            current = current.next

        print(None)

    def add_two_number(self, other):
        current_1 = self.head
        current_2 = other.head

        carry = 0

        result = LL()
        result_tail = None

        while current_1 or current_2 or carry:

            v1 = current_1.data if current_1 else 0
            v2 = current_2.data if current_2 else 0

            total = v1 + v2 + carry

            carry = total // 10
            value = total % 10

            new_node = Node(value)

            # First node
            if result.head is None:
                result.head = new_node
                result_tail = new_node

            # Remaining nodes
            else:
                result_tail.next = new_node
                result_tail = new_node

            current_1 = current_1.next if current_1 else None
            current_2 = current_2.next if current_2 else None

        return result


# First linked list
ll = LL()
ll.insert(1)
ll.insert(11)
ll.insert(111)
ll.insert(1111)

print("LL1:")
ll.print_ll()


# Second linked list
ll_2 = LL()
ll_2.insert(2)
ll_2.insert(22)
ll_2.insert(222)
ll_2.insert(2222)

print("LL2:")
ll_2.print_ll()


# Add two linked lists
res = ll.add_two_number(ll_2)

print("Result:")
res.print_ll()