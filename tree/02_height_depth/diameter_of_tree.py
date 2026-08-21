"""
Diameter of a Binary Tree - DFS with Height Tracking   (Difficulty: Medium)
Asked at: Amazon, Google, Meta

Problem:
Given the root of a binary tree, find its diameter - the number of edges on
the longest path between any two nodes in the tree. This path does not have
to pass through the root.

Example:
    Input:
            1
           / \
          2   3
         / \
        4   5
    Output: 3   (path 4 -> 2 -> 1 -> 3 has 3 edges)

    The longest path doesn't have to pass through the root either - it just
    happens to here. In general the widest path can be entirely inside a
    subtree, which is why every node needs to be checked, not just the root.

Approach:
- The longest path through any single node is leftHeight + rightHeight - the
  height of its left subtree plus the height of its right subtree (counted in
  nodes, so this sum is already the number of edges on that path).
- Compute height bottom-up with a normal post-order recursion (height of an
  empty subtree is 0), and while doing so update a running best answer with
  leftHeight + rightHeight at every node - the true diameter is the max of
  this candidate across all nodes, not just the root.
- Use a mutable container (a list with one slot) to carry the running best
  through the recursion instead of a global, since plain ints aren't
  reassignable through nested function calls without `nonlocal`.
- Edge cases: an empty tree has diameter 0, and a single node also has
  diameter 0 (no edges at all).

Time Complexity:  O(n), every node's height is computed exactly once
Space Complexity: O(h), recursion stack depth equals the tree's height
                   (worst case O(n) for a skewed tree)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter_of_tree(root):
    best = [0]

    def height(node):
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        best[0] = max(best[0], left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return best[0]


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Diameter:", diameter_of_tree(root))  # 3
