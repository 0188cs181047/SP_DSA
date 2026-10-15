"""
Merge Two Sorted Linked Lists - Two-pointer Merge   (Difficulty: Easy)
Asked at: Amazon, Microsoft, Apple

Problem:
You are given the heads of two singly linked lists, each already sorted in
non-decreasing order. Merge them into a single sorted linked list and return
its head. You should reuse the existing nodes rather than allocating new ones.

Example:
    Input:  list1 = 1 -> 2 -> 4,  list2 = 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Approach:
- Create a dummy head node so the merged list always has a stable point to
  build from, avoiding special-casing the very first node.
- Walk both lists with a tail pointer: at each step, compare the two current
  nodes and attach the smaller one to tail, then advance that list's pointer.
- Once one list runs out, attach whatever remains of the other list in one
  shot - it's already sorted, so no further comparisons are needed.
- Edge cases: either input list (or both) can be empty/None from the start.

Time Complexity:  O(n + m), where n and m are the lengths of the two lists
Space Complexity: O(1) extra space (nodes are relinked, not copied)
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

    def merge_two_lists(self, list2):
        list1 = self.head
        dummy = Node(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # Attach the remaining nodes
        tail.next = list1 if list1 is not None else list2

        # Update the head of the merged list
        self.head = dummy.next

        return self.head


# Create the first sorted linked list
ll1 = LL()
ll1.insert(1)
ll1.insert(2)
ll1.insert(4)

# Create the second sorted linked list
ll2 = LL()
ll2.insert(1)
ll2.insert(3)
ll2.insert(4)

print("List 1:")
ll1.print_ll()

print("List 2:")
ll2.print_ll()

# Merge the lists
ll1.merge_two_lists(ll2.head)

print("Merged List:")
ll1.print_ll()