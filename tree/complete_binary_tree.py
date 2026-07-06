"""
2. Complete Binary Tree

A Complete Binary Tree is a binary tree in which:

Every level is completely filled, except possibly the last level.
The nodes in the last level are filled from left to right.
    Example (Complete Binary Tree)
          1
        /   \
       2     3
      / \   /
     4   5 6

Complete Binary Tree

A Complete Binary Tree is a binary tree where every level is completely filled except possibly the last, 
and the last level is filled from left to right.

"""

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_complete(root):
    if root is None:
        return True

    queue = deque([root])
    found_null = False

    while queue:
        node = queue.popleft()

        if node is None:
            found_null = True
        else:
            if found_null:
                return False

            queue.append(node.left)
            queue.append(node.right)

    return True


# Create Complete Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(is_complete(root))