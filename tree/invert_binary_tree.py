"""
An Invert Binary Tree is a binary tree in which the left and right children of every node are swapped.

Inverting a binary tree means mirroring the tree from left to right.

Before inversion:
        4
       / \
      2   7
     / \ / \
    1  3 6  9

After inversion:
        4
       / \
      7   2
     / \ / \
    9  6 3  1

Key definition:
    An inverted binary tree is the mirror image of the original binary tree, 
    created by recursively swapping the left and right child of every node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def invertBinaryTree(self, node):
        if node is None:
            return None

        temp = node.left

        node.left = node.right
        node.right = temp

        self.invertBinaryTree(node.left)
        self.invertBinaryTree(node.right)

        return node

def traversal(node):
    if node is None:
        return None
    
    print(node.data, end="->")

    traversal(node.left)
    traversal(node.right)

if __name__ == "__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)

traversal(node=node)

s = Solution()
res = s.invertBinaryTree(node=node)
print("\n")
traversal(res)
