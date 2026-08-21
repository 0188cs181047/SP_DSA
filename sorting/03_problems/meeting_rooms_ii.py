"""
Meeting Rooms II (Minimum Rooms Required) - Sort + Min-Heap of End Times   (Difficulty: Medium)
Asked at: Amazon, Google, Meta, Goldman Sachs

Problem:
Given a list of meeting time intervals where each interval is [start, end],
find the minimum number of conference rooms required so that no two
meetings that overlap in time are ever scheduled in the same room.

Example:
    Input: intervals = [[0, 30], [5, 10], [15, 20]]
    Output: 2

    Timeline:
        Room 1: [0 ---------------------------- 30]
        Room 2:       [5 -- 10]   [15 -- 20]

Approach:
- Sort meetings by start time so they are processed in the order rooms
  would actually be needed.
- Keep a min-heap of the end times for every room currently in use; the
  heap top is always the room that frees up soonest.
- For each meeting, if the earliest-freeing room's end time is <= the
  current meeting's start time, reuse that room (pop the old end time,
  push the new one); otherwise no room is free yet, so allocate a new
  room (just push).
- The heap's final size is the peak number of rooms needed at once, which
  is the answer.
- Edge cases: empty input (0 rooms), a meeting that starts exactly when
  another ends (not an overlap, so the room can be reused), and all
  meetings sharing the same time range (needs len(intervals) rooms).

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

import heapq


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda interval: interval[0])
    end_times_heap = []  # min-heap of end times for rooms currently in use

    for start, end in intervals:
        if end_times_heap and end_times_heap[0] <= start:
            heapq.heapreplace(end_times_heap, end)
        else:
            heapq.heappush(end_times_heap, end)

    return len(end_times_heap)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(min_meeting_rooms(intervals))  # 2
