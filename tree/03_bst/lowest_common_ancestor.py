"""
Lowest Common Ancestor (Binary Tree & BST) - Recursive DFS   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Google, Meta

Problem:
Given the root of a tree and two nodes p and q that are guaranteed to exist
in it, find their lowest common ancestor (LCA) - the deepest node that has
both p and q as descendants (a node is allowed to be a descendant of
itself). Solve it two ways: once assuming the tree is a general binary tree
with no ordering guarantee, and once assuming it's a binary search tree
where value comparisons can be used to prune the search.

Example:
    Input:
            6
           / \
          2   8
         / \  / \
        0  4 7  9
        p = 0, q = 4
    Output: 2   (2 is the deepest node that has both 0 and 4 underneath it)

Approach:
- General binary tree: recurse into both children. If a subtree's recursive
  call returns p or q (or an LCA found deeper down), that result bubbles up
  unchanged. The current node is the LCA exactly when the left and right
  recursive calls each return something non-null - that means p and q were
  found on opposite sides, so this node is where their paths split.
- If only one side returns non-null, pass that result up as-is (it means
  both p and q, or just one of them so far, are in that subtree).
- BST: no need to explore both subtrees blindly. Compare the current node's
  value to p and q - if both are smaller, the LCA must be in the left
  subtree; if both are larger, it must be in the right subtree; otherwise
  (one is smaller-or-equal and the other larger-or-equal) the current node
  is the split point and therefore the LCA.
- Edge cases: if one of p or q is itself an ancestor of the other, the
  answer is that ancestor node itself (a node counts as its own ancestor).

Time Complexity:  O(n) for the general tree (may visit every node);
                   O(h) for the BST version, since each step moves down one
                   level toward the split point (worst case O(n) if skewed)
Space Complexity: O(h), recursion stack depth equals the tree's height
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowest_common_ancestor_binary_tree(root, p, q):
    if root is None or root is p or root is q:
        return root

    left = lowest_common_ancestor_binary_tree(root.left, p, q)
    right = lowest_common_ancestor_binary_tree(root.right, p, q)

    if left is not None and right is not None:
        return root

    return left if left is not None else right


def lowest_common_ancestor_bst(root, p, q):
    node = root

    while node is not None:
        if p.data < node.data and q.data < node.data:
            node = node.left
        elif p.data > node.data and q.data > node.data:
            node = node.right
        else:
            return node

    return None


if __name__ == "__main__":
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(0)
    root.left.right = Node(4)
    root.right.left = Node(7)
    root.right.right = Node(9)

    p, q = root.left.left, root.left.right  # nodes 0 and 4

    print("LCA (general tree):", lowest_common_ancestor_binary_tree(root, p, q).data)  # 2
    print("LCA (BST):", lowest_common_ancestor_bst(root, p, q).data)  # 2
