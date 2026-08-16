# Hash Table

A **Hash Table** (Hash Map) stores data as **key-value pairs**. A **hash function** converts the key into an index into an internal array, so lookup, insert, and delete average O(1) — regardless of how many items are stored.

```
key "apple"  -> hash("apple")  -> index 2 -> [ ... | ("apple", 10) | ... ]
key "banana" -> hash("banana") -> index 5 -> [ ... | ("banana", 20) | ... ]
```

## How It Works

1. A **hash function** takes a key and produces a numeric index (`hash(key) % table_size`).
2. The value is stored at that index in the underlying array.
3. To look up a key, the same hash function recomputes the index directly — no searching required.

## Collisions

Two different keys can hash to the same index — this is a **collision**. Common resolution strategies:

| Strategy | Description |
|---|---|
| Chaining | Each index holds a linked list (or list) of all key-value pairs that hashed there |
| Open Addressing | On collision, probe for the next open slot (linear probing, quadratic probing, double hashing) |

A good hash function distributes keys evenly to minimize collisions, keeping lookups close to O(1).

## Operations & Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) (many collisions) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case happens when many keys collide into the same bucket (e.g. a poor hash function, or a hostile input) — well-implemented hash tables resize and rehash to keep this rare.

## When to Use a Hash Table

- Fast lookups by key: caching, database indexing, symbol tables.
- Counting frequency of items (word counts, duplicate detection).
- Checking membership in a set quickly ("have I seen this before?").
- Mapping relationships (e.g. `student_id -> student_record`).

## When Not to Use

- You need the data in **sorted order** — a hash table has no inherent ordering (use a balanced tree/sorted structure instead).
- You need to iterate in insertion order and memory-overhead matters — a plain array/list may be simpler.

## Common Problems Solved with Hash Tables

- Two Sum (find pair summing to target in O(n))
- Detect duplicates in an array
- Group Anagrams
- First non-repeating character
- Longest Consecutive Sequence
- Implementing a cache (combined with a Linked List for LRU Cache)
