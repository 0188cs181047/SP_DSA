"""
Maximum Depth of a Binary Tree - Recursive DFS   (Difficulty: Easy)
Asked at: Amazon, Microsoft

Problem:
Given the root of a binary tree, find its maximum depth - the number of nodes
along the longest path from the root node down to the farthest leaf node.
An empty tree has a depth of 0.

Example:
    Input:
            3
           / \
          9  20
             / \
            15  7
    Output: 3

Approach:
- The depth of a tree rooted at a node is 1 (for the node itself) plus the
  larger of the depths of its left and right subtrees.
- Recurse to the base case first: an empty subtree (None) has depth 0. Every
  other call combines the results of its two children.
- Edge cases: an empty tree (root is None) returns 0, and a single node
  returns 1. A skewed tree (all left or all right children) still works since
  the recursion just walks straight down one side.

Time Complexity:  O(n), every node is visited exactly once
Space Complexity: O(h), recursion stack depth equals the tree's height
                   (worst case O(n) for a skewed tree)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth(node):
    if node is None:
        return 0

    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)

    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print("Maximum depth:", max_depth(root))  # 3
