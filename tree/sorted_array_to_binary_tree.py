"""
Convert Sorted Array to Binary Search Tree — Definition

Convert Sorted Array to Binary Search Tree (BST) means creating a height-balanced Binary Search Tree from a sorted array.

The main idea is:

Choose the middle element of the sorted array as the root.
Elements on the left side become the left subtree.
Elements on the right side become the right subtree.
Repeat the same process recursively for both halves.

Sorted Array:
[-10, -3, 0, 5, 9]

              0
            /   \
          -3     5
         /        \
       -10         9

Time Complexity: O(n)
Space Complexity: O(n) for the resulting tree, or O(log n) auxiliary recursion space for a balanced tree.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def sortedArraytoBianrySearchTree(self, array):
        def helper(l, r):
            if l > r:
                return None

            m = (l+r)//2
            node = Node(array[m])
            node.left = helper(l, m-1)
            node.right = helper(m+1, r)

            return node
        
        return helper(0, len(array)-1)

def traversal(node):
    if node is None:
        return 
    
    print(node.data, end="->")

    traversal(node=node.left)
    traversal(node=node.right)

if __name__ == "__main__":
    sorted_array = [-10, -3, 0, 5, 9]
    s = Solution()
    res = s.sortedArraytoBianrySearchTree(array=sorted_array)
    traversal(res)
