"""
Task Scheduler with Cooldown - Greedy + Max-Heap with a Cooldown Queue   (Difficulty: Medium)
Asked at: Amazon, Meta, Uber

Problem:
Given a list of tasks (represented as characters) and a non-negative
integer `cooldown`, find the minimum number of time units needed to
finish all tasks such that the same task type is never run twice within
`cooldown` units of each other. The CPU may sit idle in a unit if no task
is currently eligible to run.

Example:
    Input:  tasks = ["A", "A", "A", "B", "B", "B"], cooldown = 2
    Output: 8

    schedule: A -> B -> idle -> A -> B -> idle -> A -> B
    time:     1    2      3     4    5      6     7    8

    heap [A:3, B:3] --run A--> cooldown queue [(A, ready@3)]
       ^                                              |
       |__________ pushed back once ready@3 <= now ___|

Approach:
- Always run the most frequent *available* task next - that's the greedy
  part: burning down the task with the most remaining copies first leaves
  the most breathing room for it to cool down again before it is needed.
- Use a max-heap (min-heap of negated counts) to always grab that most
  frequent available task in O(log k) time, where k is the number of
  distinct task types.
- After running a task, it can't run again for `cooldown` units, so it
  can't go straight back into the heap. Push it into a FIFO cooldown
  queue instead, holding (task, remaining_count, time_it_becomes_available
  _again). Every tick, check the front of that queue - once its ready
  time has arrived, pop it and push it back into the heap so it can
  compete for "most frequent" again.
- The loop simply advances time one unit at a time until both the heap
  and the cooldown queue are empty; idle units where the heap is empty
  but the queue isn't (waiting on a cooldown) still tick the clock,
  which is exactly how the idle gaps show up in the answer.
- Edge cases: cooldown = 0 means no waiting is ever needed, so the answer
  degenerates to just the total task count; a task that reaches count 0
  is simply never pushed back into the heap or the cooldown queue.

Time Complexity:  O(n log k), where n is the total scheduled length
                   returned (including idle units) and k is the number
                   of distinct task types - each unit does at most one
                   O(log k) heap pop/push
Space Complexity: O(k) for the heap and the cooldown queue
"""

import heapq
from collections import Counter, deque


def least_interval(tasks, cooldown):
    counts = Counter(tasks)
    max_heap = [(-count, task) for task, count in counts.items()]
    heapq.heapify(max_heap)

    time = 0
    resting = deque()  # each entry: (task, remaining_count, ready_time)

    while max_heap or resting:
        time += 1

        if max_heap:
            neg_count, task = heapq.heappop(max_heap)
            remaining = neg_count + 1  # one instance of this task just ran
            if remaining < 0:
                resting.append((task, remaining, time + cooldown))

        if resting and resting[0][2] == time:
            task, remaining, _ = resting.popleft()
            heapq.heappush(max_heap, (remaining, task))

    return time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    cooldown = 2
    print("tasks:", tasks, "cooldown:", cooldown)
    print("minimum time units:", least_interval(tasks, cooldown))
    # 8
