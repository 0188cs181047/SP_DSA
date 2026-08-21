"""
Binary Tree Right/Left Side View - Level Order (BFS)   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Meta

Problem:
Given the root of a binary tree, return the values of the nodes visible when
the tree is viewed from the right side, ordered top to bottom (one value per
level - whatever node is rightmost at that depth). The left side view is the
mirror of this: the leftmost node visible at each depth.

Example:
    Input:
            1
           / \\
          2   3
         /     \\
        4       5
    Output: Right view = [1, 3, 5], Left view = [1, 2, 4]

    At depth 0 only node 1 exists, so it appears in both views. At depth 1,
    node 3 is the last one seen scanning left to right (right view) and node
    2 is the first (left view). At depth 2, only 4 and 5 exist, one per
    branch, so each view picks up whichever one is present.

Approach:
- Do a standard level-order BFS, processing one full level (a fixed-size
  batch popped from the queue) at a time so each level's boundary is known.
- Within a level, the first node dequeued is the leftmost node at that depth
  and the last node dequeued is the rightmost - so track the loop index
  against the level's size to capture both in a single pass.
- Both views can be built together in one traversal instead of running BFS
  twice, since the same level-by-level scan produces both boundaries.
- Edge cases: an empty tree returns empty views. A tree that is a single
  straight line (only left children, or only right children) makes the two
  views diverge the most - one view stays length 1, the other grows with
  every level.

Time Complexity:  O(n), every node is dequeued and examined exactly once
Space Complexity: O(w), where w is the widest level of the tree - that is
                   the most nodes the queue ever holds at once
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_side_views(root):
    if root is None:
        return [], []

    right_view = []
    left_view = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                left_view.append(node.data)
            if i == level_size - 1:
                right_view.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_view, left_view


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    right_view, left_view = tree_side_views(root)
    print("Right view:", right_view)  # [1, 3, 5]
    print("Left view:", left_view)    # [1, 2, 4]
