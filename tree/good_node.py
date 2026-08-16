"""
A node is good if its value is greater than or equal to the maximum value among all nodes on the path from the root to that node.

        3
       / \
      1   4
     / \   \
    3   2   5

3 → Good, because it is the root.
1 → Not good, because ancestor 3 > 1.
4 → Good, because 4 >= 3.
3 (left child of 1) → Good, because ancestors are 3, 1 and 3 >= max(3,1).
2 → Not good, because ancestor 3 > 2.
5 → Good, because 5 >= max(3,4).

X is Good
if X >= maximum value of its ancestors

"""


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def goodNode(self, node):
        def dfs(node, max_val):
            if node is None:
                return 0
            
            res = 1 if node.data >= max_val else 0

            max_val = max(max_val, node.data)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)

            return res

        return dfs(node=node, max_val=node.data)


if __name__ == "__main__":
    node = Node(3)
    node.left = Node(1)
    node.right = Node(4)
    node.left.left = Node(3)
    node.right.right = Node(5)
    node.right.right = Node(6)

s = Solution()
res = s.goodNode(node=node)
print(res)