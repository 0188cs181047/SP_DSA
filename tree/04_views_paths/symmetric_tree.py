"""
Symmetric Tree Check - Mirrored Recursion   (Difficulty: Easy)
Asked at: Amazon, Microsoft

Problem:
Given the root of a binary tree, determine whether it is a mirror of itself -
that is, the left subtree is a mirror reflection of the right subtree. A
tree is symmetric if, at every level, the values read the same from the
outside in on both sides.

Example:
    Input:
            1
           / \\
          2   2
         / \\ / \\
        3  4 4  3
    Output: True

    Input:
            1
           / \\
          2   2
           \\   \\
            3   3
    Output: False   (both 3's hang on the right, so the shapes don't mirror)

Approach:
- Symmetry is a property of a pair of subtrees, not a single tree, so the
  recursion needs to compare two nodes at once - start with (root.left,
  root.right) rather than recursing on one node at a time.
- Two subtrees are mirrors of each other when their root values match AND
  the first one's left subtree mirrors the second one's right subtree AND
  the first one's right subtree mirrors the second one's left subtree - the
  cross-comparison (left-with-right) is what makes it a mirror check instead
  of a plain equality check.
- Base cases: two Nones are a trivial mirror (True); one None and one real
  node can never mirror (False); mismatched values also fail immediately.
- Edge cases: an empty tree and a single-node tree are both symmetric by
  definition, since there's nothing on either side to conflict.

Time Complexity:  O(n), every node is visited exactly once across both sides
Space Complexity: O(h), recursion stack depth equals the tree's height
                   (worst case O(n) for a skewed tree)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_symmetric(root):
    def is_mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.data != right.data:
            return False

        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    if root is None:
        return True

    return is_mirror(root.left, root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    print("Is symmetric:", is_symmetric(root))  # True

    lopsided_root = Node(1)
    lopsided_root.left = Node(2)
    lopsided_root.right = Node(2)
    lopsided_root.left.right = Node(3)
    lopsided_root.right.right = Node(3)

    print("Is symmetric:", is_symmetric(lopsided_root))  # False
