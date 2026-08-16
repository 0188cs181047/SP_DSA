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
