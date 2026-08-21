"""
Allocate Minimum Number of Pages / Painter's Partition Problem - Binary Search on the Answer + Greedy Feasibility Check   (Difficulty: Hard)
Asked at: Amazon, Google, Directi

Problem:
Given an array of n books where books[i] is the number of pages in the i-th
book, and an integer m representing the number of students, allocate all
books to the m students such that every book is assigned to exactly one
student, each student gets a contiguous run of books, and the maximum
number of pages assigned to any single student is minimized. Return that
minimized maximum. (This is the same problem as the Painter's Partition
Problem, with "pages" swapped for "boards" and "students" for "painters".)

Example:
    Input:  books = [12, 34, 67, 90], m = 2
    Output: 113   (split as [12, 34, 67] and [90] -> max(113, 90) = 113,
                    which is the best achievable split into 2 groups)

Approach:
- The answer (the minimized maximum load) is bounded below by max(books)
  (one student must take the single largest book) and bounded above by
  sum(books) (one student takes everything). As the candidate max-load
  increases from that lower bound to the upper bound, the minimum number
  of students required to stay within it monotonically decreases - a
  classic monotonic condition that makes binary search on the answer
  applicable.
- For a candidate max-load "limit", greedily walk the books left to right,
  adding each book to the current student's running total as long as it
  fits within limit; when adding the next book would exceed limit, start a
  new student. Count how many students this greedy split needs.
- If the required student count is <= m, "limit" is feasible, so it becomes
  a candidate answer and we try to shrink it further (search the lower
  half). If it needs more than m students, "limit" is too small, so we
  search the upper half.
- Edge cases: if m >= number of books, every book can get its own student,
  so the answer is simply max(books); the binary search handles this
  naturally since the feasibility check would already succeed at
  limit = max(books).

Time Complexity:  O(n log(sum(books))) - each of the O(log(sum)) binary
                   search steps runs an O(n) feasibility scan
Space Complexity: O(1) - the feasibility check uses only a running total
                   and a counter
"""


def students_required(books, limit):
    students = 1
    current_load = 0

    for pages in books:
        if current_load + pages > limit:
            students += 1
            current_load = pages
        else:
            current_load += pages

    return students


def allocate_min_pages(books, m):
    low, high = max(books), sum(books)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if students_required(books, mid) <= m:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


if __name__ == "__main__":
    books = [12, 34, 67, 90]
    m = 2
    print("Books:", books, "Students:", m)
    print("Minimum possible max pages assigned:", allocate_min_pages(books, m))

    books = [10, 20, 30, 40]
    m = 2
    print("Books:", books, "Students:", m)
    print("Minimum possible max pages assigned:", allocate_min_pages(books, m))
