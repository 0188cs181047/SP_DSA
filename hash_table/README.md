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

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [../logical](../logical) | Two Sum | [two_sum.py](../logical/two_sum.py) | HashMap | Easy | Amazon, Google, Microsoft, Meta, Adobe |
| 2 | [01_basics](01_basics) | Implement a HashMap from Scratch (Chaining) | [implement_hashmap.py](01_basics/implement_hashmap.py) | Buckets + Chaining | Medium | Amazon, Google, TCS |
| 3 | [02_frequency_counting](02_frequency_counting) | Group Anagrams | [group_anagrams.py](02_frequency_counting/group_anagrams.py) | HashMap keyed by signature | Medium | Amazon, Meta, Microsoft, Uber |
| 4 | [02_frequency_counting](02_frequency_counting) | Top K Frequent Elements | [top_k_frequent_elements.py](02_frequency_counting/top_k_frequent_elements.py) | HashMap + Heap/Bucket Sort | Medium | Amazon, Meta, Google |
| 5 | [02_frequency_counting](02_frequency_counting) | First Non-Repeating Character | [first_non_repeating_char.py](02_frequency_counting/first_non_repeating_char.py) | HashMap Frequency Count | Easy | Amazon, Microsoft, TCS, Infosys |
| 6 | [03_subarray_membership](03_subarray_membership) | Longest Consecutive Sequence | [longest_consecutive_sequence.py](03_subarray_membership/longest_consecutive_sequence.py) | HashSet | Medium | Amazon, Meta, Google |
| 7 | [03_subarray_membership](03_subarray_membership) | Contains Duplicate II (within distance k) | [contains_duplicate_ii.py](03_subarray_membership/contains_duplicate_ii.py) | HashMap of last-seen index | Easy | Amazon, Google |
| 8 | [04_advanced](04_advanced) | Isomorphic Strings | [isomorphic_strings.py](04_advanced/isomorphic_strings.py) | Two HashMaps | Easy | Amazon, Google |
| 9 | [../linked_list](../linked_list/05_advanced) | Design an LRU Cache | [lru_cache.py](../linked_list/05_advanced/lru_cache.py) | HashMap + Doubly Linked List | Medium/Hard | Amazon, Google, Meta, Uber |

## How to Pick the Right Pattern in an Interview

- Need O(1) existence checks or counting? → **HashMap / HashSet**
- Need to group items by some derived signature (anagram letters, remainder, etc.)? → **HashMap keyed by that signature**
- Need "top-k" or "most/least frequent"? → **Frequency HashMap + Heap** (or bucket sort)
- Need O(1) get/put with an eviction order? → **HashMap + Doubly Linked List** (LRU Cache)
- Need to detect a run/streak among scattered numbers? → **HashSet membership checks**

## Folder Structure

```
hash_table/
├── README.md
├── 01_basics/                 # Implement a HashMap from scratch
├── 02_frequency_counting/     # Group Anagrams, Top K Frequent, First Non-Repeating Char
├── 03_subarray_membership/    # Longest Consecutive Sequence, Contains Duplicate II
└── 04_advanced/               # Isomorphic Strings (+ Two Sum, LRU Cache — cross-linked above)
```

Run any file directly to see it work, e.g.:

```bash
python 02_frequency_counting/group_anagrams.py
```
