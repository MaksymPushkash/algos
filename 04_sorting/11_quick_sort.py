# Implementation of QuickSort
def quicksort(arr, s, e):
    if e - s + 1 <= 1:
        return

    pivot = arr[e]
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quicksort(arr, s, left - 1)

    # Quick sort right side
    quicksort(arr, left + 1, e)

    return arr


'''
SUGGESTED PROBLEMS

https://leetcode.com/problems/sort-an-array/

https://leetcode.com/problems/kth-largest-element-in-an-array/
'''