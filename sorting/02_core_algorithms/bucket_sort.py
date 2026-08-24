"""
Bucket Sort - Distribute Into Buckets, Sort Each   (Difficulty: Medium)
Asked at: Amazon, Bloomberg

Problem:
Given an array of floating-point numbers uniformly distributed over
[0, 1), sort it in ascending order by scattering elements into several
"buckets", sorting each bucket individually, then concatenating them.

Example:
    Input:  [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]
    Output: [0.12, 0.17, 0.21, 0.26, 0.39, 0.72, 0.78, 0.94]

Approach:
- Create n empty buckets. For each element, compute which bucket it
  belongs to via `int(n * value)` - since values are uniform over
  [0, 1), this spreads them roughly evenly across buckets.
- Sort each bucket independently (insertion sort works well since
  buckets are expected to be small), then concatenate the buckets in
  order - each bucket only contains values less than the next bucket's,
  so no merging step is needed beyond concatenation.
- Edge cases: empty input (returns immediately). Performance degrades
  to O(n^2) if the input isn't actually uniform (e.g. all values land
  in one bucket), since bucket sort's average-case guarantee relies on
  that distribution assumption.

Time Complexity:  O(n + k) average (uniform input, k buckets), O(n^2) worst case
Space Complexity: O(n + k) for the buckets
"""


def bucket_sort(arr):
    if not arr:
        return arr

    n = len(arr)
    buckets = [[] for _ in range(n)]

    for value in arr:
        index = int(n * value)
        if index == n:  # guard against value == 1.0 landing out of range
            index = n - 1
        buckets[index].append(value)

    for bucket in buckets:
        _insertion_sort(bucket)

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def _insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


if __name__ == "__main__":
    nums = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]
    print("Before:", nums)
    print("After: ", bucket_sort(nums))
