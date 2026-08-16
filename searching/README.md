# Searching

**Searching** algorithms find whether a target value exists in a collection, and if so, where.

## Linear Search

Check every element one by one until the target is found or the collection ends.

```
[5, 3, 8, 1, 9]  search for 8
 ^  ^  ^
 5  3  8 -> found at index 2
```

| | Complexity |
|---|---|
| Time | O(n) |
| Space | O(1) |
| Works on | Any collection, sorted or not |

## Binary Search

Repeatedly split a **sorted** collection in half, discarding the half that can't contain the target.

```
[1, 3, 5, 7, 9, 11]  search for 7

low=0, high=5, mid=2 -> arr[2]=5 < 7 -> search right half
low=3, high=5, mid=4 -> arr[4]=9 > 7 -> search left half
low=3, high=3, mid=3 -> arr[3]=7 == 7 -> found!
```

| | Complexity |
|---|---|
| Time | O(log n) |
| Space | O(1) iterative, O(log n) recursive (call stack) |
| Requires | Collection must be sorted |

Binary search is dramatically faster than linear search: searching 1,000,000 sorted items takes at most ~20 comparisons instead of up to 1,000,000.

## Comparison

| | Linear Search | Binary Search |
|---|---|---|
| Requires sorted data | No | Yes |
| Time Complexity | O(n) | O(log n) |
| Best for | Small or unsorted data | Large, sorted, static data |

## When to Use

- **Linear Search**: data is unsorted, small, or you're searching a linked list (no random access for binary search).
- **Binary Search**: data is sorted (or can be sorted once and searched many times), and fast repeated lookups matter.

## Common Problems Solved with Searching

- Find an element's index in a sorted array
- Find the first/last occurrence of a target (lower bound / upper bound)
- Search in a rotated sorted array
- Find the square root of a number (binary search on the answer)
- Find peak element
