"""
Binary Tree Zigzag Level Order Traversal - BFS + Direction Flag   (Difficulty: Medium)
Asked at: Amazon, Microsoft, Bloomberg

Problem:
Given the root of a binary tree, return its node values arranged in level
order, but alternating direction between levels: the first level reads
left-to-right, the second right-to-left, the third left-to-right again, and
so on.

Example:
    Input:      3
               / \
              9  20
                /  \
               15    7
    Output: [[3], [20, 9], [15, 7]]

Approach:
- A plain level-order BFS already visits nodes level by level - the only
  change needed for zigzag order is to flip the direction every other level.
- Collect each level into a list the normal way (left-to-right, following
  queue order), then reverse that list before appending it to the result
  whenever the level index is odd. A boolean flag toggled after every level
  avoids needing to check the index directly.
- Edge cases: an empty tree returns []; a single-node tree returns [[val]]
  since there's no second level to reverse.

Time Complexity:  O(n) - every node is enqueued and dequeued exactly once
Space Complexity: O(n) - the queue holds up to one full level, result holds all nodes
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_values = []
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level_values.reverse()
        result.append(level_values)
        left_to_right = not left_to_right

    return result


if __name__ == "__main__":
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Zigzag level order:", zigzag_level_order(root))
