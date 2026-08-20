"""
Clone Graph   (Difficulty: Medium)
Asked at: Google, Meta, Amazon — classic "deep copy a graph" question

Problem:
Given a reference to a node in a connected undirected graph, return a
deep copy (clone) of the graph — new node objects, same structure.

Example graph:
    1 --- 2
    |     |
    4 --- 3

Flow (DFS with a hash map from original node -> cloned node):
    clone(1): create copy of 1, map{1: copy1}
      for neighbor 2: not cloned yet -> clone(2), copy1.neighbors.append(copy2)
        clone(2): create copy of 2, map{1:copy1, 2:copy2}
          for neighbor 1: ALREADY in map -> just link copy2.neighbors.append(copy1)
          for neighbor 3: not cloned -> clone(3)...
      ...continues until every node is cloned exactly once

Approach:
- The tricky part is cycles/shared references — you must clone each
  original node exactly ONCE, or you'll recurse forever.
- Use a hash map {original_node: cloned_node}. Before cloning a node,
  check the map — if it's already there, reuse the clone instead of
  creating a new one and reuse it to build the neighbor list.
- BFS works just as well as DFS here — either traversal + the hash map
  is the actual trick, not the traversal order.

Time Complexity:  O(V + E)
Space Complexity: O(V) for the hash map (plus the cloned graph itself).
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if node is None:
        return None

    cloned = {}

    def dfs(original):
        if original in cloned:
            return cloned[original]

        copy = Node(original.val)
        cloned[original] = copy

        for neighbor in original.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)


def build_sample_graph():
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    return n1


def print_graph(start):
    visited = set()

    def dfs(node):
        if node.val in visited:
            return
        visited.add(node.val)
        neighbor_vals = [n.val for n in node.neighbors]
        print(f"{node.val} -> {neighbor_vals}")
        for neighbor in node.neighbors:
            dfs(neighbor)

    dfs(start)


if __name__ == "__main__":
    original = build_sample_graph()
    cloned = clone_graph(original)

    print("Original graph:")
    print_graph(original)

    print("\nCloned graph (new objects, same structure):")
    print_graph(cloned)

    print("\nAre they the same object?", original is cloned)
