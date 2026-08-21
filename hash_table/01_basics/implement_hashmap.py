"""
Implement a HashMap from Scratch (Chaining) - Array of Buckets + Chaining   (Difficulty: Medium)
Asked at: Amazon, Google, TCS

Problem:
Implement a hash map (dictionary) from scratch without using Python's built-in
dict. Support put(key, value), get(key), and remove(key), each averaging O(1)
time. Store the data as an array of buckets, and handle two different keys
landing in the same bucket (a collision) by chaining - keeping a small list of
(key, value) pairs in that bucket. Grow the array and rehash everything once
the map gets too full, so buckets don't turn into long, slow-to-scan chains.

Example:
    Input:  put("apple", 1); put("banana", 2); put("cherry", 3)
            get("banana")
            remove("apple")
            get("apple")
    Output: get("banana") -> 2
            remove("apple") -> 1
            get("apple") -> raises KeyError (no longer present)

    capacity = 4, three entries stored, bucket 2 has a collision:

        index:      0            1            2                  3
                  [empty]     [empty]   [("cherry",3)] -> [("banana",2)]   [empty]
                                          (chained: cherry and banana both
                                           hashed to bucket 2)

Approach:
- bucket_index = hash(key) % capacity picks which bucket a key belongs to.
  Two different keys can hash to the same index (a collision); each bucket
  is just a Python list of (key, value) pairs, so colliding keys simply pile
  up ("chain") in the same bucket instead of overwriting each other.
- put/get/remove all hash the key once to jump straight to its bucket, then
  linearly scan that bucket (normally tiny, ideally length 1) looking for a
  matching key. put() overwrites the value in place if the key already
  exists there, otherwise appends a new (key, value) pair.
- Track size (number of stored pairs) against capacity (number of buckets).
  When the load factor size / capacity crosses a threshold (0.75 here),
  double the capacity and rehash every existing pair into the new, bigger
  bucket array - bucket index depends on capacity, so old indices are no
  longer valid and everything must be re-placed.
- Edge cases: put() on a key that already exists must update its value
  in place, not add a duplicate entry (size does not change); get()/remove()
  on a missing key raise KeyError, mirroring Python's own dict; resizing
  must rehash ALL entries, not just move them, since capacity changed.

Time Complexity:  O(1) average case for put/get/remove (amortized - occasional
                   resizes cost O(n) but are spread across n operations).
                   O(n) worst case if every key collides into one bucket.
Space Complexity: O(n) for n stored key-value pairs, plus O(capacity) for the
                   (mostly empty) bucket array itself.
"""


class HashMap:
    def __init__(self, initial_capacity=8, load_factor_threshold=0.75):
        self.capacity = initial_capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.load_factor_threshold = load_factor_threshold

    def _bucket_index(self, key, capacity):
        return hash(key) % capacity

    def put(self, key, value):
        index = self._bucket_index(key, self.capacity)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > self.load_factor_threshold:
            self._resize()

    def get(self, key):
        index = self._bucket_index(key, self.capacity)
        bucket = self.buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        raise KeyError(key)

    def remove(self, key):
        index = self._bucket_index(key, self.capacity)
        bucket = self.buckets[index]

        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                self.size -= 1
                return value

        raise KeyError(key)

    def contains(self, key):
        index = self._bucket_index(key, self.capacity)
        bucket = self.buckets[index]
        return any(existing_key == key for existing_key, _ in bucket)

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        # Every entry must be rehashed - bucket_index depends on capacity,
        # so an entry's old bucket index is no longer necessarily correct.
        for bucket in old_buckets:
            for key, value in bucket:
                new_index = self._bucket_index(key, self.capacity)
                self.buckets[new_index].append((key, value))

    def __len__(self):
        return self.size


if __name__ == "__main__":
    hash_map = HashMap(initial_capacity=4)

    hash_map.put("apple", 1)
    hash_map.put("banana", 2)
    hash_map.put("cherry", 3)

    print("get('banana'):", hash_map.get("banana"))          # 2
    print("contains('cherry'):", hash_map.contains("cherry"))  # True

    hash_map.put("apple", 10)                                # update, not a new entry
    print("get('apple') after update:", hash_map.get("apple"))  # 10
    print("size after update:", len(hash_map))               # 3

    print("remove('apple'):", hash_map.remove("apple"))       # 10
    print("contains('apple') after remove:", hash_map.contains("apple"))  # False

    try:
        hash_map.get("apple")
    except KeyError as exc:
        print("get('apple') after remove raised KeyError:", exc)

    print("\nTriggering a resize by inserting enough entries...")
    print("capacity before:", hash_map.capacity)
    for i in range(20):
        hash_map.put("key%d" % i, i)
    print("capacity after inserting 20 more entries:", hash_map.capacity)
    print("size after inserting 20 more entries:", len(hash_map))
    print("get('key17') still correct after resize:", hash_map.get("key17"))  # 17
