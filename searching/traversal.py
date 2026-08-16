from collections import deque

"""
A traversal tree usually refers to the order in which the nodes of a tree data structure are visited. 
Tree traversal is the process of systematically visiting every node exactly once
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
1. Depth-First Traversal (DFS)
DFS explores a branch as deeply as possible before backtracking.

        A
       / \
      B   C
     / \ / \
    D  E F  G

"""

"""
a) Preorder Traversal (Root → Left → Right)

Visit the root first, then the left subtree, then the right subtree.

A → B → D → E → C → F → G
"""

def preorder_traversal(node):
    if node is None:
        return
    print(node.data, end="->")
    preorder_traversal(node=node.left)
    preorder_traversal(node=node.right)

"""
b) Inorder Traversal (Left → Root → Right)

Visit the left subtree, then the root, then the right subtree.

D → B → E → A → F → C → G
"""
def inorder_traversal(node):
    if node is None:
        return 
    
    inorder_traversal(node=node.left)
    print(node.data, end="->")
    inorder_traversal(node=node.right)

"""
c) Postorder Traversal (Left → Right → Root)

Visit the left subtree, then the right subtree, and finally the root.

D → E → B → F → G → C → A
"""

def postorder_traversal(node):
    if node is None:
        return
    
    postorder_traversal(node=node.left)
    postorder_traversal(node=node.right)
    print(node.data, end='->')


"""
2. Breadth-First Traversal (BFS) / Level Order Traversal

BFS visits nodes level by level from top to bottom.

Traversal order:

A → B → C → D → E → F → G
"""

def level_order(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end="->")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.left = Node("F")
    root.right.right = Node("G")

    print("\n*************** Preorder Traversal ***************")
    preorder_traversal(root)

    print("\n*************** Inorder Traversal ***************")
    inorder_traversal(root)

    print("\n*************** Postorder Traversal ***************")
    postorder_traversal(root)

    print("\n*************** Level Order ***************")
    level_order(root)
