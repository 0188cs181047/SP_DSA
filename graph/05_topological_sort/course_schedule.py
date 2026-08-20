"""
Course Schedule I & II   (Difficulty: Medium)
Asked at: Google, Meta, Amazon, Microsoft — direct application of topological sort

Problem:
There are `numCourses` courses labeled 0..n-1. `prerequisites[i] = [a, b]`
means you must take course b before course a.
  - Course Schedule I:  can you finish ALL courses? (yes/no)
  - Course Schedule II: return ONE valid order to take all courses,
                        or [] if impossible.

Example:
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]

Flow diagram (edge b -> a means "b before a"):
    0 --> 1 --+
    |         v
    +-------> 2 --> 3

    Valid order: 0, 1, 2, 3

Approach:
- This is exactly Course Schedule = "is there a cycle in the prerequisite
  graph?" (I) + "give me the topological order" (II).
- Build a directed graph from prerequisites, run Kahn's algorithm.
- If Kahn's algorithm processes fewer than numCourses nodes, there's a
  cycle -> impossible (return False / []).
- Otherwise the BFS order IS a valid course order.

Time Complexity:  O(V + E) where V = numCourses, E = len(prerequisites)
Space Complexity: O(V + E)
"""

from collections import defaultdict, deque


def can_finish(num_courses, prerequisites):
    return len(_topo_order(num_courses, prerequisites)) == num_courses


def find_order(num_courses, prerequisites):
    order = _topo_order(num_courses, prerequisites)
    return order if len(order) == num_courses else []


def _topo_order(num_courses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(c for c in range(num_courses) if in_degree[c] == 0)
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return order


if __name__ == "__main__":
    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    print("Can finish all courses?", can_finish(num_courses, prerequisites))
    print("A valid course order:", find_order(num_courses, prerequisites))

    impossible = [[0, 1], [1, 0]]  # 0 needs 1, 1 needs 0 -> cycle
    print("Can finish (cyclic case)?", can_finish(2, impossible))
