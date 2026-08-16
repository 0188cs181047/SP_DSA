# Sorting

**Sorting** algorithms arrange elements of a collection into a defined order (ascending or descending).

## Common Algorithms

| Algorithm | Time (Best) | Time (Average) | Time (Worst) | Space | Stable? |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

**Stable** means equal elements keep their original relative order after sorting — this matters when sorting records by one field but wanting ties to preserve a prior order (e.g. sort by last name, ties keep original first-name order).

## How the Main Ones Work

**Bubble Sort** — repeatedly compare adjacent elements and swap if out of order; largest element "bubbles" to the end each pass.

**Insertion Sort** — build a sorted portion one element at a time, inserting each new element into its correct position among the already-sorted elements. Fast on nearly-sorted data.

**Merge Sort** (Divide & Conquer) — split the array in half recursively, sort each half, then merge the two sorted halves back together. Guarantees O(n log n) even in the worst case, at the cost of O(n) extra space.

```
[5, 3, 8, 1]
   split           -> [5, 3]     [8, 1]
   split           -> [5][3]     [8][1]
   merge (sorted)  -> [3, 5]     [1, 8]
   merge (sorted)  -> [1, 3, 5, 8]
```

**Quick Sort** (Divide & Conquer) — pick a **pivot**, partition elements into "less than pivot" and "greater than pivot", then recursively sort each partition. Fast in practice (good cache locality, in-place), but worst case O(n²) on already-sorted or adversarial input if the pivot is chosen poorly.

## Which to Use

- **Insertion Sort** — small or nearly-sorted arrays.
- **Merge Sort** — need guaranteed O(n log n) and stability; external sorting (data doesn't fit in memory).
- **Quick Sort** — general-purpose, in-memory sorting where average-case speed matters more than worst-case guarantees. (Most language built-ins use a hybrid, e.g. Timsort in Python.)
- **Heap Sort** — need O(n log n) worst case with O(1) extra space, stability doesn't matter.

## Common Problems Solved with Sorting

- Sort an array of 0s, 1s, and 2s (Dutch National Flag)
- Merge intervals
- Kth largest/smallest element (via Quickselect, related to Quick Sort's partition step)
- Sort a nearly-sorted array
- Custom sorting with comparators (e.g. sort strings by length then alphabetically)
