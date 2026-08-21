"""
Boundary Traversal of a Binary Tree - Left Boundary + Leaves + Right Boundary   (Difficulty: Medium)
Asked at: Amazon, Paytm, Flipkart

Problem:
Given the root of a binary tree, return the values of its "boundary" nodes in
anti-clockwise order starting from the root: the root itself, then the left
edge going top-down, then all leaf nodes left-to-right, then the right edge
going bottom-up. No node should be printed twice.

Example:
    Input:        1
                 /   \\
                2     3
               / \\  / \\
              4   5 6   7
    Output: [1, 2, 4, 5, 6, 7, 3]

Approach:
- Split the boundary into three independent passes and concatenate them,
  being careful never to double-count a node that is also a leaf or the root:
  the left edge (root's left subtree, top-down, stopping before any leaf),
  all leaves left-to-right, and the right edge (root's right subtree,
  bottom-up, stopping before any leaf).
- The left edge is walked greedily: from a node, if it's a leaf stop (leaves
  are handled separately), otherwise record it and step to its left child if
  one exists, else its right child. The right edge is the mirror image
  (prefer right, fall back to left) but has to be collected on a stack first
  since it needs to be emitted bottom-up.
- Leaves are found with a straightforward recursive scan of the whole tree,
  which naturally visits them in left-to-right order.
- Edge cases: a single-node tree is just that node (it is both root and a
  leaf, so it's returned once); if the root has no left child, the left-edge
  pass simply contributes nothing (same for a missing right child).

Time Complexity:  O(n) - the left edge, right edge, and leaf scan each touch a node at most once
Space Complexity: O(h) recursion/stack depth for the leaf scan and right-edge stack, O(n) for the result
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(node):
    return node.left is None and node.right is None


def add_left_boundary(node, result):
    while node is not None and not is_leaf(node):
        result.append(node.val)
        node = node.left if node.left is not None else node.right


def add_leaves(node, result):
    if node is None:
        return
    if is_leaf(node):
        result.append(node.val)
        return
    add_leaves(node.left, result)
    add_leaves(node.right, result)


def add_right_boundary(node, result):
    stack = []
    while node is not None and not is_leaf(node):
        stack.append(node.val)
        node = node.right if node.right is not None else node.left
    while stack:
        result.append(stack.pop())


def boundary_traversal(root):
    if root is None:
        return []
    if is_leaf(root):
        return [root.val]

    result = [root.val]
    add_left_boundary(root.left, result)
    add_leaves(root.left, result)
    add_leaves(root.right, result)
    add_right_boundary(root.right, result)
    return result


if __name__ == "__main__":
    #          1
    #        /   \
    #       2     3
    #      / \   / \
    #     4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Boundary traversal:", boundary_traversal(root))
