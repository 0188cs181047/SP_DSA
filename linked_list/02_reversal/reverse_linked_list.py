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
      if head:
        current = head
      elif self.head:
        current = self.head
      else:
        return None
      
      while current:
        print(current.data, end ="->")
        current = current.next
      print(None)

    def reverse_iterative(self):
      prev = None
      curr = self.head

      while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

      return prev


    def reverse_recursive(self):
      re_re = self._reverse(self.head)
      return re_re

    def _reverse(self, head):
        if head is None or head.next is None:
            return head
        
        new_head = self._reverse(head.next)

        head.next.next = head
        head.next = None

        return new_head


ll = LL()
ll.insert(1)
ll.insert(111)
ll.insert(1111)
ll.insert(11111)
ll.insert(111111)

ll.print_ll()

reverse = ll.reverse_iterative()

ll.print_ll(head=reverse)

# re_reverse = ll.reverse_recursive()
# ll.print_ll(head=re_reverse)
