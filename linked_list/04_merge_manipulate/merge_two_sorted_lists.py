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


def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2

    return dummy.next


if __name__ == "__main__":
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])

    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)

    merged = merge_two_lists(list1, list2)
    print("Merged:")
    print_linked_list(merged)  # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
