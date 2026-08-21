"""
Serialize and Deserialize a Binary Tree - Preorder DFS + Null Sentinels   (Difficulty: Hard)
Asked at: Amazon, Google, Microsoft, Meta

Problem:
Design an algorithm to convert a binary tree into a string (serialize) and to
convert that string back into the same binary tree structure (deserialize).
The two functions should be inverses of each other - no information about the
tree's shape or values may be lost in the round trip.

Example:
    Input:  1
           / \
          2   3
             / \
            4   5
    Output: serialize(root) -> "1,2,N,N,3,4,N,N,5,N,N"
            deserialize("1,2,N,N,3,4,N,N,5,N,N") -> the same tree structure

    Preorder walk with a sentinel for every missing child:
        1 -> 2 -> (None -> "N") -> (None -> "N") -> 3 -> 4 -> "N" -> "N" -> 5 -> "N" -> "N"

Approach:
- A preorder walk (node, then left, then right) that writes an explicit sentinel
  token ("N") whenever it steps into a null child fully encodes the tree's shape,
  not just its values - two different trees never produce the same token stream.
- Deserializing just replays the same order: pull tokens one at a time from a
  single iterator so the recursive calls for left and right always resume where
  the previous call left off, rebuilding the tree in exactly the order it was
  written.
- Edge cases: an empty tree serializes to a single "N" token and deserializes
  back to None; using an iterator (rather than an index into a list) avoids
  needing to track/return a position through every recursive call.

Time Complexity:  O(n) for both serialize and deserialize (each node visited once)
Space Complexity: O(n) for the token string/list, plus O(h) recursion stack
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    tokens = []

    def dfs(node):
        if node is None:
            tokens.append("N")
            return
        tokens.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(tokens)


def deserialize(data):
    tokens = iter(data.split(","))

    def build():
        val = next(tokens)
        if val == "N":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()


def tree_to_nested_list(root):
    # helper just for printing/verifying in the demo below
    if root is None:
        return None
    return [root.val, tree_to_nested_list(root.left), tree_to_nested_list(root.right)]


if __name__ == "__main__":
    #         1
    #        / \
    #       2   3
    #          / \
    #         4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    data = serialize(root)
    print("Serialized:", data)

    rebuilt = deserialize(data)
    print("Rebuilt tree (nested list form):", tree_to_nested_list(rebuilt))
    print("Round trip matches:", serialize(rebuilt) == data)
