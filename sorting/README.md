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
| Shell Sort | O(n log n) | O(n^1.3) (gap-dependent) | O(n²) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Yes |
| Radix Sort | O(d(n + b)) | O(d(n + b)) | O(d(n + b)) | O(n + b) | Yes |
| Bucket Sort | O(n + k) | O(n + k) | O(n²) | O(n + k) | Yes |

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

**Selection Sort** — repeatedly scan the unsorted portion for its minimum and swap it into place at the front. Always O(n²) comparisons regardless of input order, but at most O(n) swaps — useful when writes are expensive.

**Shell Sort** — an extension of insertion sort that first compares/moves elements far apart (a large "gap"), shrinking the gap each pass down to 1. Fixes insertion sort's weakness of only moving elements one step at a time.

**Heap Sort** — build a max-heap from the array, then repeatedly extract the max to the end. O(n log n) worst case with O(1) extra space.

**Counting Sort** (non-comparison) — count occurrences of each value in a bounded range, then write values out in order using those counts. Only worth it when the value range is close to n.

**Radix Sort** (non-comparison) — repeatedly counting-sort by each digit, from least to most significant, relying on the stability of counting sort to build up the final order.

**Bucket Sort** — scatter elements (typically uniformly distributed floats) into buckets by value, sort each bucket individually, then concatenate.

## Which to Use

- **Insertion Sort** — small or nearly-sorted arrays.
- **Merge Sort** — need guaranteed O(n log n) and stability; external sorting (data doesn't fit in memory).
- **Quick Sort** — general-purpose, in-memory sorting where average-case speed matters more than worst-case guarantees. (Most language built-ins use a hybrid, e.g. Timsort in Python.)
- **Heap Sort** — need O(n log n) worst case with O(1) extra space, stability doesn't matter.
- **Selection Sort** — writes are expensive and swaps must be minimized; teaching/simplicity.
- **Shell Sort** — want better-than-insertion-sort performance without merge/quick sort's extra space or recursion.
- **Counting Sort / Radix Sort** — integer keys over a bounded/known range; need linear time and stability.
- **Bucket Sort** — data is uniformly distributed over a known range (e.g. floats in [0, 1)).

## Common Problems Solved with Sorting

- Sort an array of 0s, 1s, and 2s (Dutch National Flag)
- Merge intervals
- Kth largest/smallest element (via Quickselect, related to Quick Sort's partition step)
- Sort a nearly-sorted array
- Custom sorting with comparators (e.g. sort strings by length then alphabetically)

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_basics](01_basics) | Bubble Sort | [bubble_sort.py](01_basics/bubble_sort.py) | Comparison Sort | Easy | TCS, Infosys, Wipro |
| 2 | [01_basics](01_basics) | Merge Sort | [merge_sort.py](01_basics/merge_sort.py) | Divide & Conquer | Medium | Amazon, Microsoft, Google |
| 3 | [01_basics](01_basics) | Squares of a Sorted Array | [sqare_of_merge_sort.py](01_basics/sqare_of_merge_sort.py) | Merge-style Divide & Conquer | Easy/Medium | Amazon |
| 4 | [02_core_algorithms](02_core_algorithms) | Quick Sort | [quick_sort.py](02_core_algorithms/quick_sort.py) | Divide & Conquer + Partition | Medium | Amazon, Google, Microsoft |
| 5 | [02_core_algorithms](02_core_algorithms) | Insertion Sort | [insertion_sort.py](02_core_algorithms/insertion_sort.py) | Build Sorted Prefix | Easy | TCS, Infosys, Amazon |
| 6 | [02_core_algorithms](02_core_algorithms) | Heap Sort | [heap_sort.py](02_core_algorithms/heap_sort.py) | Max-Heap Extraction | Medium | Google, Amazon, Bloomberg |
| 7 | [02_core_algorithms](02_core_algorithms) | Counting Sort | [counting_sort.py](02_core_algorithms/counting_sort.py) | Frequency Counting | Easy/Medium | Amazon, Google |
| 8 | [02_core_algorithms](02_core_algorithms) | Selection Sort | [selection_sort.py](02_core_algorithms/selection_sort.py) | Repeated Min Selection | Easy | TCS, Infosys, Wipro |
| 9 | [02_core_algorithms](02_core_algorithms) | Shell Sort | [shell_sort.py](02_core_algorithms/shell_sort.py) | Gapped Insertion Sort | Medium | Amazon, Microsoft |
| 10 | [02_core_algorithms](02_core_algorithms) | Radix Sort | [radix_sort.py](02_core_algorithms/radix_sort.py) | Digit-by-Digit Bucketing | Medium | Amazon, Google |
| 11 | [02_core_algorithms](02_core_algorithms) | Bucket Sort | [bucket_sort.py](02_core_algorithms/bucket_sort.py) | Distribute Into Buckets | Medium | Amazon, Bloomberg |
| 12 | [03_problems](03_problems) | Kth Largest Element in an Array | [kth_largest_element.py](03_problems/kth_largest_element.py) | Quickselect / Heap | Medium | Amazon, Google, Meta, Microsoft |
| 13 | [03_problems](03_problems) | Meeting Rooms II | [meeting_rooms_ii.py](03_problems/meeting_rooms_ii.py) | Sort + Min-Heap | Medium | Amazon, Google, Meta, Goldman Sachs |
| 14 | [03_problems](03_problems) | Sort a Nearly Sorted (K-Sorted) Array | [sort_k_sorted_array.py](03_problems/sort_k_sorted_array.py) | Min-Heap of size K+1 | Medium | Amazon, Microsoft |
| 15 | [04_advanced](04_advanced) | Largest Number Formed From an Array | [largest_number_from_array.py](04_advanced/largest_number_from_array.py) | Custom Comparator Sort | Medium | Amazon, Google |

## How to Pick the Right Pattern in an Interview

- Need a simple, stable sort for small or nearly-sorted data? → **Insertion Sort**
- Need guaranteed O(n log n) with stability, or external sorting? → **Merge Sort**
- Need a fast general-purpose in-memory sort? → **Quick Sort**
- Need O(n log n) worst case with O(1) space, stability doesn't matter? → **Heap Sort**
- Value range is small and bounded? → **Counting Sort** (or **Radix Sort** for larger integers, digit by digit)
- Data is uniformly distributed floats over a known range? → **Bucket Sort**
- Want simple in-place sorting with minimal swaps or better-than-O(n²) practical performance without extra space? → **Selection Sort** / **Shell Sort**
- Need the kth largest/smallest without fully sorting? → **Quickselect** or a size-k heap
- Need to schedule or merge overlapping ranges? → **Sort by start + sweep**, or a min-heap of end times

## Folder Structure

```
sorting/
├── README.md
├── 01_basics/            # Bubble Sort, Merge Sort, Squares of a Sorted Array
├── 02_core_algorithms/   # Quick, Insertion, Heap, Counting, Selection, Shell, Radix, Bucket Sort
├── 03_problems/          # Kth Largest Element, Meeting Rooms II, Sort K-Sorted Array
└── 04_advanced/          # Largest Number From an Array
```

Run any file directly to see it work, e.g.:

```bash
python 01_basics/bubble_sort.py
```
