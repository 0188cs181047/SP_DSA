"""
Find the Middle of a Linked List - Slow/Fast Pointers   (Difficulty: Easy)
Asked at: Amazon, Microsoft

Problem:
Given the head of a singly linked list, return the middle node. If the
list has an even number of nodes, return the second of the two middle
nodes. Do this in a single pass without counting the length first.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
    Output: Node with data 3

    Input:  1 -> 2 -> 3 -> 4 -> None
    Output: Node with data 3   (the second of the two middle nodes)

Flow (fast moves 2 steps for every 1 step of slow):
    slow=1 fast=1
    slow=2 fast=3
    slow=3 fast=5 (fast.next is None) -> stop, slow is the middle

Approach:
- Use two pointers starting at head: slow advances one node at a time,
  fast advances two nodes at a time.
- By the time fast reaches the end of the list (or falls off, i.e.
  becomes None), slow has covered exactly half the distance, so it's
  sitting on the middle node.
- The loop condition "while fast and fast.next" naturally produces the
  second middle node for even-length lists, since fast runs out of room
  one step earlier than a strict "reach the last node" check would.
- Edge cases: a single-node list returns that node immediately (fast
  starts as None.next check short-circuits); an empty list returns None.

Time Complexity:  O(n) - one pass over the list
Space Complexity: O(1) - only two pointers used
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


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    odd_list = build_linked_list([1, 2, 3, 4, 5])
    print("Middle of [1,2,3,4,5]:", find_middle(odd_list).data)

    even_list = build_linked_list([1, 2, 3, 4])
    print("Middle of [1,2,3,4]:", find_middle(even_list).data)
