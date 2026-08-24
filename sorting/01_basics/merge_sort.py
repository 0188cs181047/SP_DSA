"""
Merge Sort — Definition

Merge Sort is a divide-and-conquer sorting algorithm that divides an array into smaller halves, recursively sorts each half, and then merges the sorted halves to produce a completely sorted array.

Main Idea
Divide the array into two halves.
Recursively sort each half.
Merge the two sorted halves.
Continue until the entire array is sorted.

[5, 3, 8, 1]

Divide:
[5, 3]    [8, 1]

Divide:
[5] [3]   [8] [1]

Merge:
[3, 5]    [1, 8]

Final Merge:
[1, 3, 5, 8]

Time Complexity: O(n log n) — Best, Average, and Worst Case
Space Complexity: O(n) — requires extra space for merging
Stable: Yes, when implemented appropriately

"""
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left_half = array[:mid]
    right_half = array[mid:]

    sort_left = merge_sort(left_half)
    sort_right = merge_sort(right_half)

    return sort(sort_left, sort_right)

def sort(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    array = [-1, 3, 2, -4, 1]

    res = merge_sort(array=array)
    print(res)