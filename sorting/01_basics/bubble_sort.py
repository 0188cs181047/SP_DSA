"""
def:
    Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order until the entire array is sorted.

Time Complexity: O(n²) average and worst case
Best Case: O(n) with an optimized implementation
Space Complexity: O(1)


[5, 3, 8, 1]

Compare 5 and 3 → swap
[3, 5, 8, 1]

Compare 5 and 8 → no swap
[3, 5, 8, 1]

Compare 8 and 1 → swap
[3, 5, 1, 8]

"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 2, 23, 1, 7]
res = bubbleSort(arr=arr)
print(res)
