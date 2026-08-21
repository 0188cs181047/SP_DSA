# Tree

A **Tree** is a hierarchical, non-linear data structure made up of **nodes** connected by **edges**. It starts from a single **root node**, and every other node is connected via exactly one path from the root — there are no cycles.

```
        1            <- root
       / \
      2   3           <- children of 1
     / \   \
    4   5   6         <- leaves (no children)
```

## Key Terms

| Term | Meaning |
|---|---|
| Root | The topmost node, with no parent |
| Parent / Child | A node directly connected one level above/below |
| Leaf | A node with no children |
| Edge | The connection between a parent and a child |
| Height | Longest path from a node down to a leaf |
| Depth | Distance from the root to a given node |
| Subtree | A tree formed by a node and all its descendants |

## Binary Trees

A **Binary Tree** is a tree where every node has at most 2 children (`left` and `right`). This repo covers the common special cases:

| Type | File | Rule |
|---|---|---|
| Full Binary Tree | [full_binary_tree.py](full_binary_tree.py) | Every node has exactly 0 or 2 children — none have just 1 |
| Complete Binary Tree | [complete_binary_tree.py](complete_binary_tree.py) | Every level is fully filled except possibly the last, which fills left to right |
| Perfect Binary Tree | [perfect_binary_tree.py](perfect_binary_tree.py) | Every internal node has 2 children AND all leaves are at the same depth |
| Balanced Binary Tree | [balance_binary_tree.py](balance_binary_tree.py) | For every node, `\|height(left) - height(right)\| <= 1` |

Note: every **Perfect** tree is also **Complete** and **Full**, but not every **Complete**/**Full** tree is **Perfect**.

## Tree Traversal

Traversal is the process of visiting every node exactly once, in some order. See [traversal.py](../searching/traversal.py) (it lives in the `searching/` folder in this repo, but the code is Binary Tree traversal).

**Depth-First (DFS)** — go deep before backtracking:
- **Preorder** (Root → Left → Right) — used to copy/serialize a tree
- **Inorder** (Left → Root → Right) — visits a Binary Search Tree in sorted order
- **Postorder** (Left → Right → Root) — used to safely delete/free a tree bottom-up

**Breadth-First (BFS) / Level Order** — visit level by level, using a queue.

## Time Complexity

| Operation | Average (Balanced) | Worst (Unbalanced / Skewed) |
|---|---|---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Traversal (any type) | O(n) | O(n) |

## Why Trees Matter

- Represent hierarchical data naturally: file systems, org charts, DOM/HTML, JSON.
- Binary Search Trees keep data sorted and support fast search/insert/delete.
- Balanced trees (AVL, Red-Black) guarantee O(log n) operations even in the worst case.
- Tries speed up prefix search (autocomplete). Heaps (a tree-based structure) power priority queues.

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | (root) | Tree Traversal — Preorder/Inorder/Postorder/Level Order | [traversal.py](../searching/traversal.py) | DFS & BFS | Easy | Amazon, Microsoft, TCS |
| 2 | (root) | Invert a Binary Tree | [invert_binary_tree.py](invert_binary_tree.py) | Recursive DFS | Easy | Google, Amazon, Microsoft |
| 3 | (root) | Merge Two Binary Trees | [merge_two_binary_tree.py](merge_two_binary_tree.py) | Recursive DFS | Easy | Amazon, Meta |
| 4 | (root) | Good Nodes in a Binary Tree | [good_node.py](good_node.py) | DFS + Running Max | Medium | Amazon, Google |
| 5 | (root) | Convert Sorted Array to a Balanced BST | [sorted_array_to_binary_tree.py](sorted_array_to_binary_tree.py) | Divide & Conquer | Medium | Amazon, Microsoft, Google |
| 6 | [02_height_depth](02_height_depth) | Maximum Depth of a Binary Tree | [max_depth.py](02_height_depth/max_depth.py) | Recursive DFS | Easy | Amazon, Microsoft |
| 7 | [02_height_depth](02_height_depth) | Diameter of a Binary Tree | [diameter_of_tree.py](02_height_depth/diameter_of_tree.py) | DFS + Height Tracking | Medium | Amazon, Google, Meta |
| 8 | [03_bst](03_bst) | Validate a Binary Search Tree | [validate_bst.py](03_bst/validate_bst.py) | Range-bounded DFS | Medium | Amazon, Microsoft, Google |
| 9 | [03_bst](03_bst) | Kth Smallest Element in a BST | [kth_smallest_in_bst.py](03_bst/kth_smallest_in_bst.py) | Inorder Traversal | Medium | Amazon, Google |
| 10 | [03_bst](03_bst) | Lowest Common Ancestor (Binary Tree & BST) | [lowest_common_ancestor.py](03_bst/lowest_common_ancestor.py) | Recursive DFS | Medium | Amazon, Microsoft, Google, Meta |
| 11 | [04_views_paths](04_views_paths) | Binary Tree Right/Left Side View | [tree_side_view.py](04_views_paths/tree_side_view.py) | Level Order (BFS) | Medium | Amazon, Microsoft, Meta |
| 12 | [04_views_paths](04_views_paths) | Path Sum / Root-to-Leaf Paths | [path_sum.py](04_views_paths/path_sum.py) | DFS + Path Tracking | Easy/Medium | Amazon, Microsoft |
| 13 | [04_views_paths](04_views_paths) | Symmetric Tree Check | [symmetric_tree.py](04_views_paths/symmetric_tree.py) | Mirrored Recursion | Easy | Amazon, Microsoft |
| 14 | [05_advanced](05_advanced) | Serialize and Deserialize a Binary Tree | [serialize_deserialize.py](05_advanced/serialize_deserialize.py) | Preorder + Null Sentinels | Hard | Amazon, Google, Microsoft, Meta |
| 15 | [05_advanced](05_advanced) | Zigzag Level Order Traversal | [zigzag_traversal.py](05_advanced/zigzag_traversal.py) | BFS + Direction Flag | Medium | Amazon, Microsoft, Bloomberg |
| 16 | [05_advanced](05_advanced) | Boundary Traversal of a Binary Tree | [boundary_traversal.py](05_advanced/boundary_traversal.py) | 3-part DFS | Medium | Amazon, Paytm, Flipkart |

Note: [full_binary_tree.py](full_binary_tree.py), [complete_binary_tree.py](complete_binary_tree.py),
[perfect_binary_tree.py](perfect_binary_tree.py) and [balance_binary_tree.py](balance_binary_tree.py)
(the structural-property checks) are already covered in the "Binary Trees" table above.

## How to Pick the Right Pattern in an Interview

- Need to visit every node in a specific order? → **DFS** (pre/in/post) or **BFS** (level order)
- Need height, depth, or diameter? → Bottom-up recursive DFS that returns height
- Working with a BST and need order, kth-element, or validity? → **Inorder traversal** or range-bounded recursion
- Need "the view from one side" or a level-grouped result? → **BFS level order**
- Need to reconstruct/transmit a tree, or check mirror structure? → Preorder DFS with null sentinels / mirrored recursion

## Folder Structure

```
tree/
├── README.md
├── full_binary_tree.py, complete_binary_tree.py, perfect_binary_tree.py,
│   balance_binary_tree.py, invert_binary_tree.py, merge_two_binary_tree.py,
│   good_node.py, sorted_array_to_binary_tree.py   # basics & construction
├── 02_height_depth/    # Max Depth, Diameter
├── 03_bst/              # Validate BST, Kth Smallest, Lowest Common Ancestor
├── 04_views_paths/      # Side View, Path Sum, Symmetric Tree
└── 05_advanced/          # Serialize/Deserialize, Zigzag Traversal, Boundary Traversal

(Traversal — Preorder/Inorder/Postorder/Level Order — lives in ../searching/traversal.py)
```

Run any file directly to see it work, e.g.:

```bash
python 05_advanced/serialize_deserialize.py
```
