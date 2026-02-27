'''
Intervals


'''



'''
252. Meeting rooms



Given an array of meeting time intervals where intervals[i] = [start, end], determine if a person could attend all meetings.

Example 1:
Input: invervals = [[0, 30], [5, 10], [15, 20]]
Output: false

Example 2:
Input: intervals = [[7, 10], [2, 4]]
Output: true


constraints:

0 <= intervals.length <= 10^4
invervals[i].length == 2
0 <= start < end <= 10^4


перше що треба зробити це відсортувати по почаку мітинга, по даті початку мітинга

коли вони не пересікаються, то початок наступного мітинга, відбувається після кінця минулого


складність O(NlogN) через сортування
'''
from typing import List

def canAttendMeetings(intervals: List[List[int]]) -> None:
    intervals.sort()

    for i in range(1, len(intervals)):
        prev = intervals[i-1]
        current = intervals[i]

        if current[0] < prev[1]: # якщо старт поточного менший за кінець минулого
            return False
    
    return True

# =======================================================================================================================





'''
56. Merge intervals


Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.




'''


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current = intervals[i]
        prev = merged[-1]

        if current[0] <= prev[1]:
            merged[-1][1] = max(prev[1], current[1])
        else:
            merged.append(current)
    
    return merged


# =======================================================================================================================


'''
ДЗ


57. Insert Interval


You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
 still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105


треба зрозуміти куди вставити цей новий інтервал, треба його поставити на правильне місце, а потім merge зробити

'''


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    pass