
def consolidateWindows(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize the result
    result = [intervals[0]]

    # Step 3: Process remaining intervals
    for i in range(1, len(intervals)):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        last_end = result[-1][1]

        # Step 4: Merge overlapping intervals
        if current_start <= last_end:
            result[-1][1] = max(last_end, current_end)
        else:
            result.append(intervals[i])

    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(consolidateWindows(intervals))
