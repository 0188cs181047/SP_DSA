"""
Check if a Linked List is a Palindrome - Fast/Slow Pointers + Reverse Second Half   (Difficulty: Easy/Medium)
Asked at: Amazon, Meta

Problem:
Given the head of a singly linked list, determine whether it reads the same forwards
and backwards - i.e. whether it is a palindrome. Return True or False. Try to solve it
using O(1) extra space instead of copying the values into an array.

Example:
    Input:  1 -> 2 -> 2 -> 1
    Output: True

    Input:  1 -> 2 -> 3
    Output: False

    original:  1 -> 2 -> 2 -> 1
    slow/fast walk to the middle, then the second half is reversed in place:
               1 -> 2 -> None   <-   2 <- 1
               (first half)          (second half, reversed)
    comparing node by node: 1 == 1, 2 == 2 -> palindrome

Approach:
- Use the classic slow/fast pointer trick to find the middle of the list in one pass -
  fast moves two steps for every one step slow takes.
- Reverse the second half of the list in place (same technique as reversing a whole
  list), then walk the first half and the reversed second half together, comparing
  values as you go.
- If every pair matches, it's a palindrome; stop early the moment a mismatch is found.
- Edge cases: an empty list or a single node is trivially a palindrome; for an
  odd-length list, fast lands on the last node and slow lands on the true middle,
  which sits between the two halves and doesn't need to be compared against anything.
- Restoring the list afterward (re-reversing the second half) is good practice in an
  interview if asked to leave the input unmodified, though it's skipped here for clarity.

Time Complexity:  O(n)
Space Complexity: O(1) extra space (the list is relinked, not copied)
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


def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find the middle using slow/fast pointers.
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half, starting at slow (the middle).
    second_half = reverse_list(slow)

    # Compare the first half against the reversed second half.
    first = head
    second = second_half
    result = True
    while second is not None:
        if first.val != second.val:
            result = False
            break
        first = first.next
        second = second.next

    return result


if __name__ == "__main__":
    palindrome_list = build_linked_list([1, 2, 2, 1])
    print_linked_list(palindrome_list)
    print(is_palindrome(palindrome_list))  # True

    non_palindrome_list = build_linked_list([1, 2, 3])
    print_linked_list(non_palindrome_list)
    print(is_palindrome(non_palindrome_list))  # False
