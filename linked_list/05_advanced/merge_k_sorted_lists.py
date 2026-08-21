"""
Merge K Sorted Linked Lists - Min-Heap   (Difficulty: Hard)
Asked at: Amazon, Google, Microsoft

Problem:
You are given an array of k singly linked lists, each already sorted in ascending
order. Merge all of them into a single sorted linked list and return its head.

Example:
    Input:  lists = [1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6]
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

    heap always holds one candidate node per non-exhausted list:
        list0: 1 -> 4 -> 5
        list1: 1 -> 3 -> 4        heap = {1(list0), 1(list1), 2(list2)}
        list2: 2 -> 6
    pop the smallest, append to result, push its .next (if any), repeat.

Approach:
- Repeatedly merging two lists at a time works but re-scans the same nodes
  over and over; a min-heap instead tracks the current smallest candidate across
  all k lists at once.
- Push the head of every non-empty list into the heap, keyed by value. Also push a
  tie-breaking counter alongside each node, since heapq compares tuples element by
  element and ListNode objects aren't comparable when two values are equal.
- Pop the smallest entry, attach that node to the result via a tail pointer, and if
  that node has a .next, push it into the heap so its list stays represented.
- Edge cases: the input array can be empty, and individual lists inside it can be
  None/empty - both are naturally skipped since nothing gets pushed for them.

Time Complexity:  O(n log k), where n is the total number of nodes and k is the
                   number of lists (each push/pop touches a heap of size <= k)
Space Complexity: O(k) for the heap
"""

import heapq


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


def merge_k_lists(lists):
    heap = []
    counter = 0

    for node in lists:
        if node is not None:
            heapq.heappush(heap, (node.val, counter, node))
            counter += 1

    dummy = ListNode(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next


if __name__ == "__main__":
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6]),
    ]

    for i, lst in enumerate(lists):
        print("List {}:".format(i))
        print_linked_list(lst)

    merged = merge_k_lists(lists)
    print("Merged:")
    print_linked_list(merged)  # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None
