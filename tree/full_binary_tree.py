"""
A Full Binary Tree is a binary tree in which every node has either 0 or 2 children. In other words, no node has only one child.

Interview Definition

A Full Binary Tree is a binary tree where every internal (non-leaf) node has exactly two children, and every leaf node has no children.

Example of a Full Binary Tree
        A
       / \
      B   C
     / \ / \
    D  E F  G
"""
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def is_full_binary_tree(root):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is not None:
        return (is_full_binary_tree(root=root.left) and is_full_binary_tree(root=root.right))

    return False
        

node = Node("A")
node.left = Node("B")
node.right = Node("C")
node.left.left = Node("D")
node.left.right = Node("E")
node.right.left = Node("F")
node.right.right = Node("G")

res = is_full_binary_tree(root=node)

if res:
    print(f"Tree is full binary tree {res}")
else:
    print(f"Tree is not full binary tree {res}")