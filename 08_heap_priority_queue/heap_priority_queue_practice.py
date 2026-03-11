'''
Priority Queue
черга з якимось приорітетом

це структура даних, в яку ми можему вставляти/забирати по високому/низькому приорітетом

в Prioority Queue є багато реалізацій, одна з них це Binary Heap

(виглядає як дерево, але по факту це масив).

Binary Heap буває двох видів, max heap та min heap


для того, щоб дерево, назвалось binary heap, є умова, що воно повинно бути complete.
complete означає, що кожен поверх має бути максимально заповнений зліва на право, і ми не переходимо на наступний поверх, 
    поки не заповнили поточний поверх.


для того щоб це була max heap, значення в ноді має бути більше ніж в її дітей

min heap навпаки


є операція heapify, коли ми готовий масив перетворюємо в хіпу, відбувається за O(n)

в python реалізована тільки min heap.

min heap можна векористовувати ще й як max heap, ось таки чином:
arr = [4, 1, 5, 8, 19, 0, 12]
max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)


-----
max_heap -> [-19, -8, -12, -1, -5, 0, -4]


'''


'''
215.  Kth largest element in a array


Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4



логічно буде просто відсортувати по зростанню і взяти к-тий з кінця 

але в цій задачі Can you solve it without sorting?


будемо вирішувати через min heap
мінімальна хіпа з самих максимальних

'''
from typing import List, Optional
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]

# ==============================================================================================================================

'''
703. Kth Largest element in a stream

You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time.
 This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns
 the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the
   sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool
 of test scores so far.

 

Тобто в нас є stream, якийсь поток даних.
 
В нас є потік оцінок, і нам треба зберігати к-ту максимальну оцінку в класі. І при цьому в нас нові оцінки можуть приходити і приходити. 
І ми на кожному кроці маємо віддавати к-ту максимальну оцінку.

'''


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# ==============================================================================================================================

'''
347. Top K Frequent elements


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    c = Counter(nums)
    min_heap = []

    for num, freq in c.items():
        heapq.heappush(min_heap, (freq, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return [item[1] for item in min_heap]


# ==============================================================================================================================


'''
451. Sort Characters by frequency


Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character 
is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

'''


def frequencySort(s: str) -> str:
    c = Counter(s)
    max_heap = []

    for ch, value in c.items():
        heapq.heappush(max_heap, (-value, ch*value))

    result = ""

    while max_heap:
        result += heapq.heappop(max_heap)[1]
    
    return result



# ==============================================================================================================================


'''
1046. Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
 Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

тут max_heap
'''


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-stone for stone in stones]

    heapq.heapify(stones) # O(n)

    while len(stones) > 1:
        first = -heapq.heappop(stones)
        second = -heapq.heappop(stones)

        if first != second:
            heapq.heappush(stones, -(first - second))

    if not stones:
        return 0
    
    return -stones[0]


# ==============================================================================================================================


'''
502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, 
 LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, 
  it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital 
   after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.


Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
'''

def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    projects = sorted(list(zip(capital, profits))) # зшиваєм і сортуєм

    can_afford = []

    checked = 0

    for _ in range(k):
        while checked < len(projects) and projects[checked][0] <= w:
            heapq.heappush(can_afford, -projects[checked][1])
            checked += 1
        
        if not can_afford:
            break

        w += -heapq.heappop(can_afford)

    return w


# ==============================================================================================================================

'''
295. Find Median from data stream


The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
 and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

від нас хочуть, щоб до нас пхали безкінечно числа, но ми кожен раз могли віддати медіану

треба використовувати дві хіпи тут, одна max, інша min

для більшої частини min_heap, для меншої max_heap і тоді в нас на вершинах будуть лежати медіани



ми завжли добавляєм в макс хіпу, і завжди переливаєм в мін хіпу
'''


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None: # O(logN)
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        

    def findMedian(self) -> float: # O(1)
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]

        return (self.min_heap[0] + -self.max_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# ==============================================================================================================================


'''
ДЗ


1962. Remove Stones to minimize the total


You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k.
 You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the largest integer that is smaller than or equal to x (i.e., rounds x down).

 

Example 1:

Input: piles = [5,4,9], k = 2. Дано стопки камнів, в одній стопці 5 камнів, в другій 4 і в третрій 9
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.




'''


def minStoneSum(piles: List[int], k: int) -> int:
    heap = [-pile for pile in piles]
    heapq.heapify(heap)

    for _ in range(k):
        -heapq.heappop(heap) / 2


# ==============================================================================================================================




'''
23. Merge k Sorted lists


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6



Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    min_heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i))

    while min_heap:
        val, i = heapq.heappop(min_heap)

        current.next = lists[i]
        current = current.next

        if lists[i].next:
            lists[i] = lists[i].next
            heapq.heappush(min_heap, (lists[i].val, i))
    
    return dummy.next


# ==============================================================================================================================

