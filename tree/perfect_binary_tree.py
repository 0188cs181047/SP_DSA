""" 
A Perfect Binary Tree is a type of binary tree in which:
Every internal (non-leaf) node has exactly 2 children.
All leaf nodes are at the same level (same depth).

    Example
               1
             /   \
            2     3
           / \   / \
          4   5 6   7

Interview Definition
    A Perfect Binary Tree is a binary tree in which every internal node has exactly two children and all leaf nodes are at the same depth. 
    A perfect binary tree of height h contains 2^(h+1) - 1 total nodes and 2^h leaf nodes.
"""
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d

def is_perfect(root, depth, level=1):
    if root is None:
        return True

    # Leaf node
    if (root.left is None) and (root.right is None):
        return depth == level

    # One child only
    if (root.left is None) or (root.right is None):
        return False

    return (is_perfect(root.left, depth, level + 1) and is_perfect(root.right, depth, level + 1))

if __name__ == "__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)

    res = is_perfect(root=node, depth=calculateDepth(node=node))
    if res:
        print("Yes! It is perfect binary tree")
    else:
        print("No! It is not perfect binary tree")