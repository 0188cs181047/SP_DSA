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

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_basics](01_basics) | Linear Search | [linear_search.py](01_basics/linear_search.py) | Sequential Scan | Easy | TCS, Infosys, Wipro, Amazon |
| 2 | [01_basics](01_basics) | Binary Search (Iterative & Recursive) | [binary_search.py](01_basics/binary_search.py) | Divide & Conquer | Easy | Amazon, Google, Microsoft |
| 3 | [02_binary_search_variants](02_binary_search_variants) | First and Last Occurrence of an Element | [first_last_occurrence.py](02_binary_search_variants/first_last_occurrence.py) | Lower/Upper Bound | Medium | Amazon, Microsoft |
| 4 | [02_binary_search_variants](02_binary_search_variants) | Search Insert Position (Lower Bound) | [search_insert_position.py](02_binary_search_variants/search_insert_position.py) | Lower Bound | Easy | Amazon, Google |
| 5 | [02_binary_search_variants](02_binary_search_variants) | Search in a Rotated Sorted Array | [search_rotated_sorted_array.py](02_binary_search_variants/search_rotated_sorted_array.py) | Modified Binary Search | Medium | Amazon, Microsoft, Google, Bloomberg |
| 6 | [03_binary_search_on_answer](03_binary_search_on_answer) | Square Root of a Number | [sqrt_binary_search.py](03_binary_search_on_answer/sqrt_binary_search.py) | Binary Search on the Answer | Easy/Medium | Amazon, Microsoft |
| 7 | [03_binary_search_on_answer](03_binary_search_on_answer) | Find Peak Element | [find_peak_element.py](03_binary_search_on_answer/find_peak_element.py) | Binary Search on the Slope | Medium | Amazon, Google |
| 8 | [03_binary_search_on_answer](03_binary_search_on_answer) | Allocate Min Pages / Painter's Partition | [allocate_min_pages.py](03_binary_search_on_answer/allocate_min_pages.py) | Binary Search on the Answer + Greedy | Hard | Amazon, Google, Directi |
| 9 | [04_advanced](04_advanced) | Median of Two Sorted Arrays | [median_two_sorted_arrays.py](04_advanced/median_two_sorted_arrays.py) | Binary Search on a Partition | Hard | Amazon, Google, Microsoft, Apple |
| 10 | [04_advanced](04_advanced) | Search in a Sorted 2D Matrix | [search_2d_matrix.py](04_advanced/search_2d_matrix.py) | Binary Search / Staircase Search | Medium | Amazon, Microsoft, Google |

Note: [traversal.py](traversal.py) in this folder is actually Binary Tree traversal
code (kept here for historical reasons) — see the [Tree module](../tree/README.md)
for it as an interview topic.

## How to Pick the Right Pattern in an Interview

- Data is unsorted or small? → **Linear Search**
- Data is sorted, need an exact index or bound (first/last/insert point)? → **Binary Search variants**
- The answer isn't a direct lookup but "smallest/largest value that satisfies a feasibility check"? → **Binary Search on the Answer** + a greedy/linear feasibility check
- Two sorted structures combined (arrays or a matrix)? → **Binary search on a partition**, or a staircase walk

## Folder Structure

```
searching/
├── README.md
├── traversal.py                     # Tree traversal code (see the Tree module)
├── 01_basics/                        # Linear Search, Binary Search
├── 02_binary_search_variants/        # First/Last Occurrence, Insert Position, Rotated Array Search
├── 03_binary_search_on_answer/       # Sqrt, Find Peak, Allocate Min Pages
└── 04_advanced/                       # Median of Two Sorted Arrays, Search 2D Matrix
```

Run any file directly to see it work, e.g.:

```bash
python 04_advanced/median_two_sorted_arrays.py
```
