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

Traversal is the process of visiting every node exactly once, in some order. See [traversal.py](traversal.py).

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
