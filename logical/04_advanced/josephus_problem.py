"""
The Josephus Problem - Recursion / Circular Elimination   (Difficulty: Hard)
Asked at: Amazon, Google, Directi

Problem:
n people stand in a circle, numbered 1 to n. Starting from person 1 and
counting around the circle, every kth person is eliminated. Counting
continues around the shrinking circle until only one person remains.
Find the 1-indexed position (in the original numbering) of that last
survivor.

Example:
    Input: n = 5, k = 2
    Output: 3

Approach:
- Simulation (easiest to reason about): keep a list/queue of people. Walk
  around it with an index, and every kth step remove the person currently
  pointed at (wrapping the index around with modulo). Repeat until one
  person is left. This is O(n) removals, and removing from a plain Python
  list is O(n) each time, so it's O(n^2) overall - fine for small n and
  great for building intuition.
- Recurrence (the classic trick): define J(n, k) as the 0-indexed winning
  position when there are n people. If we know the winner's position
  J(n-1, k) among the n-1 people left *after* the first elimination, we
  can map it back to the original n-person circle by rotating forward by
  k positions (and wrapping with % n), because the first elimination
  effectively relabels the circle starting right after the eliminated
  person. That gives J(n, k) = (J(n-1, k) + k) % n, with base case
  J(1, k) = 0 (with one person left, they are the survivor at index 0).
- Convert the final 0-indexed recurrence result back to a 1-indexed
  person number by adding 1.
- Edge cases: n = 1 always returns person 1 (no eliminations needed);
  k = 1 eliminates everyone in order, so the last original person (n)
  survives.

Time Complexity:  O(n) for the recurrence version, O(n^2) for the list-based simulation
Space Complexity: O(n) for the recurrence version (call stack), O(n) for the simulation (the list of survivors)
"""


def josephus_recurrence(n, k):
    def survivor_index(count):
        if count == 1:
            return 0
        return (survivor_index(count - 1) + k) % count

    return survivor_index(n) + 1


def josephus_simulation(n, k):
    people = list(range(1, n + 1))
    idx = 0
    while len(people) > 1:
        idx = (idx + k - 1) % len(people)
        people.pop(idx)
    return people[0]


if __name__ == "__main__":
    n, k = 5, 2
    print(f"n={n}, k={k} -> survivor (recurrence):", josephus_recurrence(n, k))
    print(f"n={n}, k={k} -> survivor (simulation):", josephus_simulation(n, k))

    n, k = 7, 3
    print(f"n={n}, k={k} -> survivor (recurrence):", josephus_recurrence(n, k))
    print(f"n={n}, k={k} -> survivor (simulation):", josephus_simulation(n, k))
