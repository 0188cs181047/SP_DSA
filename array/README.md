# Array

An **Array** is a collection of elements stored in **contiguous memory**, each accessible by an **index**. It is the simplest and most widely used data structure — most other data structures are built on top of it.

```
Index:    0     1     2     3     4
Value:  [10] [ 20] [ 30] [ 40] [ 50]
```

Because elements sit next to each other in memory, the address of any element can be calculated directly:

```
address(i) = base_address + (i * size_of_element)
```

That's what makes random access O(1).

## Types

| Type | Description |
|---|---|
| Static Array | Fixed size, decided at creation (e.g. `int arr[5]` in C) |
| Dynamic Array | Resizable (e.g. Python `list`, Java `ArrayList`, C++ `vector`) — grows by reallocating to a bigger block when full |
| Multi-dimensional Array | Array of arrays, e.g. a 2D grid/matrix `arr[row][col]` |

## Operations & Time Complexity

| Operation | Time Complexity | Notes |
|---|---|---|
| Access by index | O(1) | Direct address calculation |
| Search (unsorted) | O(n) | Must check each element |
| Search (sorted, binary search) | O(log n) | Requires sorted array |
| Insert at end | O(1) amortized | O(n) if the dynamic array must resize |
| Insert at beginning/middle | O(n) | Shifts all following elements |
| Delete at end | O(1) | |
| Delete at beginning/middle | O(n) | Shifts all following elements |

## Static vs Dynamic Arrays

- A **static array** has a fixed size — inserting beyond capacity is not possible.
- A **dynamic array** starts with some capacity, and when full, allocates a new (typically 2x) block and copies all elements over — this copy is O(n), but happens rarely enough that insertion at the end is O(1) on average (**amortized**).

## When to Use Arrays

- You need **fast, random access** by index.
- The size of the collection is known or bounded.
- Cache performance matters — contiguous memory is CPU-cache friendly, making arrays faster in practice than linked structures for iteration.

## When Not to Use Arrays

- Frequent insertions/deletions in the middle of the collection — a [Linked List](../linked_list/README.md) avoids the O(n) shifting cost.
- Size is highly unpredictable and grows very large — consider a hash table or dynamic structure suited to the access pattern.

## Common Problems Solved with Arrays

- Two Pointers (e.g. pair sum in a sorted array)
- Sliding Window (e.g. max sum subarray of size k)
- Prefix Sum (range sum queries)
- Kadane's Algorithm (maximum subarray sum)
- Sorting and Binary Search

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_basics](01_basics) | Find Max/Min in an Array | [find_max_min.py](01_basics/find_max_min.py) | Single Pass | Easy | Amazon, TCS, Infosys, Capgemini |
| 2 | [01_basics](01_basics) | Reverse an Array In-Place | [reverse_array.py](01_basics/reverse_array.py) | Two Pointers | Easy | Amazon, Wipro, Accenture |
| 3 | [02_two_pointers](02_two_pointers) | Two Sum II (pair in a sorted array) | [two_sum_sorted.py](02_two_pointers/two_sum_sorted.py) | Two Pointers | Easy | Amazon, Microsoft, Google |
| 4 | [02_two_pointers](02_two_pointers) | Move Zeroes | [move_zeroes.py](02_two_pointers/move_zeroes.py) | Two Pointers | Easy | Meta, Amazon, Bloomberg |
| 5 | [02_two_pointers](02_two_pointers) | Sort Colors (Dutch National Flag) | [sort_colors.py](02_two_pointers/sort_colors.py) | Three Pointers | Medium | Microsoft, Meta, Google |
| 6 | [02_two_pointers](02_two_pointers) | Container With Most Water | [container_with_most_water.py](02_two_pointers/container_with_most_water.py) | Two Pointers | Medium | Amazon, Google, Adobe |
| 7 | [03_sliding_window](03_sliding_window) | Max Sum Subarray of Size K | [max_sum_subarray_k.py](03_sliding_window/max_sum_subarray_k.py) | Fixed Sliding Window | Easy | Amazon, Microsoft, TCS |
| 8 | [03_sliding_window](03_sliding_window) | Longest Substring Without Repeating Characters | [longest_substring_no_repeat.py](03_sliding_window/longest_substring_no_repeat.py) | Variable Sliding Window | Medium | Amazon, Meta, Bloomberg |
| 9 | [04_prefix_sum](04_prefix_sum) | Subarray Sum Equals K | [subarray_sum_equals_k.py](04_prefix_sum/subarray_sum_equals_k.py) | Prefix Sum + HashMap | Medium | Google, Meta, Amazon |
| 10 | [04_prefix_sum](04_prefix_sum) | Range Sum Query — Immutable | [range_sum_query.py](04_prefix_sum/range_sum_query.py) | Prefix Sum | Easy | Amazon, Google |
| 11 | [05_kadane](05_kadane) | Maximum Subarray Sum (Kadane's) | [kadanes_algorithm.py](05_kadane/kadanes_algorithm.py) | DP / Greedy | Medium | Amazon, Microsoft, LinkedIn |
| 12 | [05_kadane](05_kadane) | Maximum Product Subarray | [max_product_subarray.py](05_kadane/max_product_subarray.py) | Kadane Variant | Medium | Amazon, Meta |
| 13 | [06_sorting_based](06_sorting_based) | Merge Intervals | [merge_intervals.py](06_sorting_based/merge_intervals.py) | Sort + Sweep | Medium | Google, Amazon, Meta |
| 14 | [06_sorting_based](06_sorting_based) | Best Time to Buy and Sell Stock | [best_time_buy_sell_stock.py](06_sorting_based/best_time_buy_sell_stock.py) | Greedy, One Pass | Easy | Amazon, Microsoft, Bloomberg |
| 15 | [07_advanced](07_advanced) | Trapping Rain Water | [trapping_rain_water.py](07_advanced/trapping_rain_water.py) | Two Pointers / Precompute | Hard | Google, Amazon, Adobe |
| 16 | [07_advanced](07_advanced) | Next Permutation | [next_permutation.py](07_advanced/next_permutation.py) | In-place Manipulation | Medium | Amazon, Google |
| 17 | [07_advanced](07_advanced) | Rotate Array by K Steps | [rotate_array.py](07_advanced/rotate_array.py) | Cyclic Replacement | Medium | Microsoft, Amazon |

## How to Pick the Right Pattern in an Interview

- Need a pair/triplet hitting a target, and the array is sorted (or can be)? → **Two Pointers**
- Need a contiguous subarray/substring satisfying a size or uniqueness condition? → **Sliding Window**
- Need repeated range-sum queries, or "count subarrays summing to X"? → **Prefix Sum** (+ HashMap)
- Need the max/min sum of a contiguous subarray? → **Kadane's Algorithm**
- Problem involves overlapping ranges, or needs elements grouped in order first? → **Sort, then sweep**
- Need an in-place rearrangement with O(1) extra space (rotate, next permutation, partition)? → **Index tricks / reversal**

## Folder Structure

```
array/
├── README.md
├── 01_basics/            # Find Max/Min, Reverse Array
├── 02_two_pointers/      # Two Sum II, Move Zeroes, Sort Colors, Container With Most Water
├── 03_sliding_window/    # Max Sum Subarray K, Longest Substring Without Repeat
├── 04_prefix_sum/        # Subarray Sum Equals K, Range Sum Query
├── 05_kadane/            # Kadane's Algorithm, Max Product Subarray
├── 06_sorting_based/     # Merge Intervals, Best Time to Buy/Sell Stock
└── 07_advanced/          # Trapping Rain Water, Next Permutation, Rotate Array
```

Run any file directly to see it work, e.g.:

```bash
python 07_advanced/trapping_rain_water.py
```
