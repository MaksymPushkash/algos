arr = [1, 3, 3, 4, 5, 6, 7, 8]

# Python implementation of Binary Search
def binary_search(arr, target):
    L, R = 0, len(arr) - 1.   # L = 0, R = 7
    
    while L <= R:
        mid = (L + R) // 2. 

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1

'''
SUGGESTED PROBLEMS

https://leetcode.com/problems/binary-search/

https://leetcode.com/problems/search-a-2d-matrix/
'''