"""
Merge Two Binary Trees means combining two binary trees into a single binary tree by adding the values of nodes that exist at the same position.

If both trees have a node at the same position → add their values.
If only one tree has a node → keep that node as it is.
The process is performed recursively for the left and right subtrees.

Example:
    Tree 1:    1
              / \
             3   2

    Tree 2:      2
                / \
                1  3

    Merged:      3
                / \
                4  5

1 + 2 = 3
3 + 1 = 4
2 + 3 = 5

Time Complexity: O(n)
Space Complexity: O(h) for recursion, where h is the tree height.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def mergeTree(self, node1, node2):
        if node1 is None and node2 is None:
            return None

        data1 = node1.data if node1 else 0
        data2 = node2.data if node2 else 0 

        m_node = Node(data1+data2)
        m_node.left = self.mergeTree(node1.left if node1 else None, node2.left if node2 else None)
        m_node.right = self.mergeTree(node1.right if node1 else None, node2.right if node2 else None)

        return m_node


def traversal(node):
    if node is None:
        return None
    
    print(node.data, end="->")
    traversal(node.left)
    traversal(node.right)

if __name__ == "__main__":
    node1 = Node(1)
    node1.left = Node(1)
    node1.right = Node(2)

    node2 = Node(22)
    node2.left = Node(33)

    traversal(node2)
    print("\n")
    traversal(node1)

    s = Solution()
    res = s.mergeTree(node1, node2)
    print(f"\n")
    
    traversal(res)
