"""
Design a Hit Counter (last 5 minutes) - Queue of Timestamps   (Difficulty: Medium)
Asked at: Google, Amazon

Problem:
Design a hit counter that records a hit at a given timestamp (in seconds)
via `hit(timestamp)` and reports how many hits occurred in the past 300
seconds via `get_hits(timestamp)`. Calls arrive with non-decreasing
timestamps, and multiple hits can share the exact same timestamp.

Example:
    Input:  hit(1); hit(2); hit(3)
            get_hits(4)     -> 3   (all three hits are within the last 300s)
            hit(300)
            get_hits(300)   -> 4   (300 - 1 = 299 < 300, still counts)
            get_hits(301)   -> 3   (301 - 1 = 300, the hit at t=1 just expired)
    Output: 3, 4, 3

    front (oldest) -> [t=1] [t=2] [t=3] [t=300] <- back (newest)
                         |
                         v  once (now - t) >= 300, pop it off the front
                       expired, drop from the window

Approach:
- Keep every hit in a deque in the order it arrived, since timestamps only
  ever increase - that ordering means expired hits are always sitting at
  the front, so they can be dropped without scanning the whole queue.
- Before answering get_hits, pop from the front while the oldest timestamp
  is 300 seconds or more behind `timestamp`; whatever remains in the queue
  is exactly the hits still inside the trailing 5-minute window.
- Collapse consecutive hits that share the same timestamp into a single
  (timestamp, count) entry and track a running `total`. This keeps the
  queue's size bounded by the number of distinct timestamps in the window
  (not the number of raw hits), which matters if one timestamp gets
  hammered thousands of times.
- Edge cases: get_hits called before any hit() returns 0; hits and reads
  can share the exact same timestamp, and both count as "within the
  window" since the window is a strict `timestamp - t < 300`.

Time Complexity:  O(1) amortized per call - each distinct timestamp is
                   pushed once and popped at most once across all calls
Space Complexity: O(W) where W is the number of distinct timestamps
                   currently inside the trailing 300-second window
"""

from collections import deque


class HitCounter:
    def __init__(self):
        self.window = deque()  # each entry: [timestamp, count_at_that_timestamp]
        self.total = 0

    def hit(self, timestamp):
        if self.window and self.window[-1][0] == timestamp:
            self.window[-1][1] += 1
        else:
            self.window.append([timestamp, 1])
        self.total += 1

    def get_hits(self, timestamp):
        while self.window and timestamp - self.window[0][0] >= 300:
            _, expired_count = self.window.popleft()
            self.total -= expired_count
        return self.total


if __name__ == "__main__":
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print("get_hits(4):", counter.get_hits(4))      # 3

    counter.hit(300)
    print("get_hits(300):", counter.get_hits(300))  # 4
    print("get_hits(301):", counter.get_hits(301))  # 3
