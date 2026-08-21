"""
Copy a Linked List with a Random Pointer - HashMap Cloning   (Difficulty: Medium/Hard)
Asked at: Amazon, Google, Meta

Problem:
A linked list is given where each node has a "next" pointer and an additional
"random" pointer that can point to any node in the list (or to None). Return a deep
copy of the list: the new list must have entirely new nodes, but its "next" and
"random" pointers must mirror the structure of the original.

Example:
    Input:  1 -> 2 -> 3, where node(1).random = node(3), node(2).random = node(2),
            node(3).random = node(1)
    Output: A fully separate list 1' -> 2' -> 3' with node(1').random = node(3'),
            node(2').random = node(2'), node(3').random = node(1')

    original: [1] -> [2] -> [3]
                |      |      |
              random points anywhere among [1], [2], [3], or None

    clone:    [1']-> [2']-> [3']   (new nodes, same random/next shape)

Approach:
- The tricky part is that random pointers can point forward or backward, so nodes
  must exist before they can be wired up - a single pass can't fully connect things.
- First pass: walk the original list and create a clone for every node (copying only
  the value), storing a mapping from original node -> clone node in a hash map.
- Second pass: walk the original list again; for each original node, use the map to
  set clone.next = map[original.next] and clone.random = map[original.random],
  treating None as its own valid lookup (map[None] is defined as None).
- Edge cases: an empty list returns None; a node whose random pointer is None must
  map to None, not crash on a missing key.

Time Complexity:  O(n)
Space Complexity: O(n) for the hash map holding the old-node -> new-node mapping
"""


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head):
    if head is None:
        return None

    old_to_new = {None: None}

    # First pass: clone every node's value, without wiring next/random yet.
    current = head
    while current is not None:
        old_to_new[current] = Node(current.val)
        current = current.next

    # Second pass: wire up next and random pointers on the clones.
    current = head
    while current is not None:
        clone = old_to_new[current]
        clone.next = old_to_new[current.next]
        clone.random = old_to_new[current.random]
        current = current.next

    return old_to_new[head]


def build_list_with_random(values, random_indices):
    # values: list of node values. random_indices: list of same length where
    # random_indices[i] is the index (into values) the i-th node's random points to,
    # or None.
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, r in enumerate(random_indices):
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None


def print_list_with_random(head):
    current = head
    index_of = {}
    node = head
    i = 0
    while node is not None:
        index_of[node] = i
        node = node.next
        i += 1

    parts = []
    while current is not None:
        random_index = index_of[current.random] if current.random is not None else None
        parts.append("{}(random->{})".format(current.val, random_index))
        current = current.next
    print(" -> ".join(parts))


if __name__ == "__main__":
    # 1 -> 2 -> 3, with node(1).random = node(3), node(2).random = node(2),
    # node(3).random = node(1).
    original = build_list_with_random([1, 2, 3], [2, 1, 0])
    print("Original:")
    print_list_with_random(original)

    cloned = copy_random_list(original)
    print("Cloned:")
    print_list_with_random(cloned)

    # Confirm the clone is made of entirely new nodes.
    print(cloned is not original)          # True
    print(cloned.random is not original.random)  # True
