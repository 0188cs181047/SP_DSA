"""
Kth Smallest Element in a BST - Inorder Traversal   (Difficulty: Medium)
Asked at: Amazon, Google

Problem:
Given the root of a binary search tree and an integer k, find the kth
smallest value in the tree (k is 1-indexed, so k=1 asks for the smallest
value).

Example:
    Input:
            5
           / \
          3   8
         / \
        2   4
        k = 3
    Output: 4   (sorted order is 2, 3, 4, 5, 8 - the 3rd value is 4)

Approach:
- An inorder traversal (left, node, right) of a BST visits every node's
  value in strictly increasing order - that's the defining property of a
  BST's in-order sequence.
- Walk the tree inorder while keeping a counter of how many nodes have been
  visited so far. As soon as the counter reaches k, that node's value is the
  answer - stop and return immediately instead of collecting the whole
  traversal into a list, which saves both time and space on large trees.
- An iterative version using an explicit stack achieves the same early-exit
  behavior and avoids recursion depth limits on very skewed trees.
- Edge cases: k is assumed to be within [1, number of nodes], as is standard
  for this problem - no bounds checking is needed for valid input.

Time Complexity:  O(h + k), where h is the tree height to reach the leftmost
                   node plus k steps of inorder traversal (worst case O(n))
Space Complexity: O(h), the recursion/stack depth needed for the traversal
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kth_smallest(root, k):
    stack = []
    node = root
    count = 0

    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        count += 1

        if count == k:
            return node.data

        node = node.right

    return None


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)

    print("3rd smallest:", kth_smallest(root, 3))  # 4
    print("1st smallest:", kth_smallest(root, 1))  # 2
