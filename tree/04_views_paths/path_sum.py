"""
Path Sum / All Root-to-Leaf Paths - DFS with Path Tracking   (Difficulty: Easy/Medium)
Asked at: Amazon, Microsoft

Problem:
Given the root of a binary tree and a target sum, first determine whether
there exists a root-to-leaf path whose node values add up to that target.
Then, as the natural follow-up, return every root-to-leaf path (as a list of
node values) whose sum equals the target - not just whether one exists.

Example:
    Input:
                5
              /   \\
             4     8
            /     / \\
          11    13   4
         /  \\        / \\
        7    2      5   1
    target = 22
    Output: has_path_sum -> True
            all paths    -> [[5, 4, 11, 2], [5, 8, 4, 5]]

Approach:
- Push the running sum down through the recursion rather than accumulating
  totals on the way back up: subtract the current node's value from the
  target as you descend, so a leaf only needs to check whether the
  remaining amount has hit exactly 0.
- A path only counts once it reaches a true leaf (no left AND no right
  child) - reaching remaining == 0 at an internal node does not qualify,
  since the path must run root to leaf, not stop partway.
- For the "all paths" version, carry a mutable list as the current path,
  append before recursing into children, and pop it after returning
  (backtracking) so the same list object can be reused across every branch
  instead of copying it at every call.
- Edge cases: an empty tree has no root-to-leaf path at all, so it can never
  satisfy any target (even target 0). Negative node values are handled fine
  since the check is exact equality, not a range.

Time Complexity:  O(n), every node is visited exactly once
Space Complexity: O(h) for the recursion stack, plus O(h) for the path list
                   being built (h is the tree's height, worst case O(n))
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def has_path_sum(root, target_sum):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return target_sum == root.data

    remaining = target_sum - root.data
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)


def all_root_to_leaf_paths_with_sum(root, target_sum):
    result = []

    def dfs(node, remaining, path):
        if node is None:
            return

        path.append(node.data)
        remaining -= node.data

        if node.left is None and node.right is None and remaining == 0:
            result.append(list(path))
        else:
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

        path.pop()

    dfs(root, target_sum, [])
    return result


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.right.right.left = Node(5)
    root.right.right.right = Node(1)

    target = 22
    print("Has path sum:", has_path_sum(root, target))  # True
    print("All matching paths:", all_root_to_leaf_paths_with_sum(root, target))
    # [[5, 4, 11, 2], [5, 8, 4, 5]]
