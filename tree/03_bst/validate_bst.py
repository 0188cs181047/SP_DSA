"""
Validate a Binary Search Tree - Range-bounded DFS   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Google

Problem:
Given the root of a binary tree, determine whether it is a valid binary
search tree (BST). A valid BST requires that for every node, all values in
its left subtree are strictly less than the node's value, and all values in
its right subtree are strictly greater than the node's value - and this must
hold recursively for every subtree, not just the immediate children.

Example:
    Input:
            5
           / \
          3   8
         / \  / \
        1  4 7  9
    Output: True

    Input:
            5
           / \
          3   8
             / \
            4   9
    Output: False   (4 is in the right subtree of 5 but 4 < 5)

Approach:
- A node isn't valid just because it's greater than its left child and less
  than its right child - it must also respect the bounds set by every
  ancestor above it. So carry a (low, high) range down through the
  recursion: a node's value must fall strictly inside that range.
- When moving into the left child, tighten the upper bound to the current
  node's value; when moving into the right child, tighten the lower bound.
  The bounds start as (-infinity, +infinity) at the root.
- An equally valid alternative is to do an inorder traversal and check the
  resulting sequence is strictly increasing - a BST's inorder traversal is
  sorted if and only if the tree is valid.
- Edge cases: an empty tree is considered valid. Duplicate values are not
  allowed (comparisons are strict, not <=/>=).

Time Complexity:  O(n), every node is visited exactly once
Space Complexity: O(h), recursion stack depth equals the tree's height
                   (worst case O(n) for a skewed tree)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(root):
    def validate(node, low, high):
        if node is None:
            return True

        if not (low < node.data < high):
            return False

        return validate(node.left, low, node.data) and validate(node.right, node.data, high)

    return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(7)
    root.right.right = Node(9)

    print("Is valid BST:", is_valid_bst(root))  # True

    bad_root = Node(5)
    bad_root.left = Node(3)
    bad_root.right = Node(8)
    bad_root.right.left = Node(4)
    bad_root.right.right = Node(9)

    print("Is valid BST:", is_valid_bst(bad_root))  # False
