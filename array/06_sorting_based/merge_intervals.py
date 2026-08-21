"""
Merge Overlapping Intervals - Sort + Sweep   (Difficulty: Medium)
Asked at: Google, Amazon, Meta

Problem:
Given a list of intervals where each interval is [start, end], merge all
overlapping intervals and return a list of the non-overlapping intervals
that cover all the ranges in the input. Two intervals are considered
overlapping if one starts at or before the other one ends.

Example:
    Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]

    sorted:  [1,3] [2,6]      [8,10]      [15,18]
                |----|
                   |----|
             merge into [1,6]  (2 <= 3, so they overlap)

             [1,6]        [8,10]      [15,18]
             kept as-is   8 > 6, no overlap, keep separate

Approach:
- Sort intervals by start time. Once sorted, any interval that overlaps
  with the current merged run must immediately follow it, so a single
  left-to-right sweep is enough - no need to compare every pair.
- Keep a "merged" result list. For each interval, compare it against the
  last interval already placed in merged: if the current interval's start
  is <= the last interval's end, they overlap, so extend the last
  interval's end to the max of the two ends. Otherwise, the current
  interval starts a new non-overlapping group, so append it as-is.
- Edge cases: an empty input returns an empty list; a single interval
  returns itself; fully nested intervals (e.g. [1,10] then [2,3]) are
  handled correctly because we always take the max of the ends, not just
  overwrite it.

Time Complexity:  O(n log n)  (dominated by the sort)
Space Complexity: O(n)        (for the sorted copy / output list)
"""


def merge_intervals(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda pair: pair[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = [last_start, max(last_end, end)]
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_intervals(intervals))  # [[1, 6], [8, 10], [15, 18]]
