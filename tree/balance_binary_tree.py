"""
Balanced Binary Tree
    A Balanced Binary Tree is a binary tree in which, 
    for every node, the difference between the height of the left subtree and the height of the right subtree is at most 1.

    |Height(Left Subtree) - Height(Right Subtree)| <= 1

          1
        /   \
       2     3
      / \   /
     4   5 6
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def is_balance(self, root):
        def dfs(root):
            if root is None:
                return [True, 0]
            
            left = dfs(root=root.left)
            right = dfs(root=root.right)

            balance = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            return (balance, 1 + max(left[1], right[1]))

        return dfs(root=root)

if __name__ == "__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)

    s = Solution()
    res = s.is_balance(root=node)
    if res[0]:
        print("Yes! It is the balance binary tree")

    else:
        print("No!, It is not balance binary tree")