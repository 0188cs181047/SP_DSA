"""
Design and Implement an LRU Cache - Doubly Linked List + HashMap   (Difficulty: Medium/Hard)
Asked at: Amazon, Google, Meta, Uber

Problem:
Design a Least Recently Used (LRU) cache with a fixed capacity. It should support
get(key), which returns the value for key or -1 if it isn't present, and put(key,
value), which inserts or updates the value for key. Both operations must run in O(1)
time. When put() would exceed capacity, evict the least recently used entry first.
Any successful get() or put() on a key counts as "using" it, moving it to the front.

Example:
    Input:  capacity = 2
            put(1, "a"); put(2, "b")
            get(1)          -> "a"   (1 is now most recently used)
            put(3, "c")     -> evicts key 2 (the least recently used)
            get(2)          -> -1    (evicted)
    Output: "a", -1

    most recently used                     least recently used
        head <-> [2] <-> [1] <-> tail          (after put(1), put(2): 2 is MRU)
        head <-> [1] <-> [2] <-> tail          (after get(1) moves 1 to front)
        head <-> [3] <-> [1] <-> tail          (after put(3) evicts 2, the LRU)

Approach:
- A hash map alone gives O(1) key lookup but no notion of usage order; a plain list
  gives ordering but O(n) moves. Combining a hash map with a doubly linked list gets
  O(1) for both.
- Keep the doubly linked list ordered by recency: the node right after the head
  sentinel is most-recently-used, the node right before the tail sentinel is
  least-recently-used.
- The hash map stores key -> node, so a get() can jump straight to a node, unlink it,
  and re-insert it right after the head sentinel in O(1) - no scanning required.
- put() does the same move-to-front dance; if the key is new and the cache is over
  capacity afterward, unlink the node just before the tail sentinel (the LRU entry)
  and delete it from the map too.
- Using two dummy sentinel nodes (head and tail) removes every "is this the first/last
  real node" special case from the unlink/insert logic.
- Edge cases: capacity of 0 (nothing ever gets stored), put() on an existing key
  (update the value and still move it to the front), get() on a missing key (-1).

Time Complexity:  O(1) for both get() and put()
Space Complexity: O(capacity) for the hash map and the linked list nodes
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}

        # Sentinels: head.next is the most-recently-used real node,
        # tail.prev is the least-recently-used real node.
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        node = Node(key, value)
        self.key_to_node[key] = node
        self._add_to_front(node)

        if len(self.key_to_node) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.key_to_node[lru_node.key]


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, "a")
    cache.put(2, "b")
    print(cache.get(1))    # "a"  (1 becomes most recently used)

    cache.put(3, "c")      # capacity exceeded -> evicts key 2 (least recently used)
    print(cache.get(2))    # -1   (evicted)

    print(cache.get(1))    # "a"
    print(cache.get(3))    # "c"

    cache.put(4, "d")      # evicts key 1 (least recently used after the gets above)
    print(cache.get(1))    # -1   (evicted)
    print(cache.get(3))    # "c"
    print(cache.get(4))    # "d"
