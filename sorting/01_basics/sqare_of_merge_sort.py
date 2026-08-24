"""
Squares of a Sorted Array — Definition

Squares of a Sorted Array means taking a sorted array that may contain negative and positive numbers, squaring every element, and returning the squares in sorted order.

The challenge is that squaring negative numbers can change their relative order.

Input:
[-4, -2, 0, 3, 5]

Square each element:
[16, 4, 0, 9, 25]

Sorted result:
[0, 4, 9, 16, 25]

Time Complexity: O(n)
Space Complexity: O(n) for the result array.

"""
def merge_sort(array):
    if len(array) <= 1:
        return [array[0]**2]

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