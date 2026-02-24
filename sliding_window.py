'''
Pattern Sliding Window

Скользяще вікно

Дає нам O(n) по часу та константу по пам'яті.

По суті це варіація two pointers


В нас є якась колекція даних, які послідовно йдуть один за одним.
І ми в ній хочемо перевірити якусь умову, наприклад, знайти найбільшу трійку елементів, які йдуть підряд.


Ми задаємо ось цю рамку, розміром 3. Потім ми йдемо, і розглядаємо елементи тільки всередині цієї рамки.


Але може бути варіація завдання, де нам розмір рамки не дано. Наприклад, знайди таку послідовність, яка задовілняє умову.

В такому випадку, рамка спочатку 0, і ми її розширяємо, до поки умова задовільняється, 
і коли дойшли до елемента, який не підходить, ми піджимаємо цю рамку до цього елемента, знову розмір рамки 0 буде, і знову її розширяєм.




карказ sliding window:

def sliding_widow():
    begin  
    window_state 
    result

    for end in range(len(nums)):
        window_state
        window size = end - begin + 1
        if/while # window condition
            result
            window_state
            begin += 1 # shrink window

    return result


головне це зрозуміти window_state, і при якій умові ми вікно піджимаємо
'''


# ==========================================================================================


from typing import List

'''
643. Maximum Average Subarray

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.


Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000




Розмір рамки k

наприклад k = 4

і нам треба розглядати в масиві всі четвірки які йдуть підряд
[1,12,-5,-6,50,3] масив
[1,12,-5,-6] перша четвірка, рамка
[12,-5,-6,50] друга четвірка - і це буде максимальна четвірка 
[-5,-6,50,3] треть четвірка, рамка


коли рамка ссувається, ми додаєм слідуючий елемент в рамку, а перший який був, ми його забираємо




в нас є begin та end, це просто pointers, і ми проходимо ендом до кінця, а begin за ним піджимається, 
    тобто максимум ми два рази масив пройдем, один раз ендом, другий раз beginom. O(n)
'''


def findMaxAverage(nums: List[int], k: int) -> float:
    begin = 0 # початок рамки
    window_state = 0 # сума чисел в рамці
    result = float('-inf')

    for end in range(len(nums)): # початок я закріпив на 0, а кінець йде далі  
        window_state += nums[end]
        if end - begin + 1 == k:
            result = max(result, window_state)
            window_state -= nums[begin]
            begin += 1  

    return result / k


# ==========================================================================================



'''
209. Minimum Size Subarray Sum


Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


розмір вікна нам не дано, нам треба вирішити коли піджимати
'''



def minSubArrayLen(target: int, nums: List[int]) -> int:
    begin = 0
    result = float('inf')
    window_state = 0

    for end in range(len(nums)):
        window_state += nums[end]

        while window_state >= target:
            window_size = end - begin + 1
            result = min(result, window_size)
            window_state -= nums[begin]
            begin += 1

    if result == float('inf'):
        return 0
    return result



# ==========================================================================================

'''
1004. Max Consecutive Ones 3

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

тут треба взанит, що таке стан вікна, і коли нам його зжимати


тут стан вікна, це скілька 0 ми бачили
зжимати, коли кількість нулів стало більше ніж k
по факту ми завжди зберігаєм рамку в якої тільки k нулів, а як тільки нулів стало більше, ми рамку піджимаєм
'''



def longestOnes(nums: List[int], k: int) -> int:
    begin = 0
    window_state = 0 # how many zeroes
    result = 0

    for end in range(len(nums)):
        if nums[end] == 0:
            window_state += 1
        
        while window_state > k:
            if nums[begin] == 0:
                window_state += 1
            begin += 1

        result = max(result, end - begin + 1)

    return result


# ==========================================================================================


'''
1493. Longest Subarray of 1's After deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
 Return 0 if there is no such subarray.


Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.


'''



def longestSubarray(nums: List[int]) -> int:
    k = 1
    begin = 0
    window_state = 0
    result = 0

    for end in range(len(nums)):
        if nums[end] == 0:
            window_state += 1
        
        while window_state > k:
            if nums[begin] == 0:
                window_state -= 1
            begin += 1

        result = max(result, end - begin + 1)

    return result - 1


# ==========================================================================================



'''
904. Fruit into Basket

You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] 
is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However,
the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. 
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, 
you must pick exactly one fruit from every tree (including the start tree) while moving to the right.
The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

в нас є тільки дві корзини, в кожній тільки один тип фрукти, 1 2 це різні типи фрукта



Від нас хочуть послідовний підмасив, який містить 2 елемента і треба знайти його довжину.

window_state це скільки фруктів я щойно бачив


In Python, defaultdict is a subclass of the built-in dict class from the collections module.
 It automatically assigns a default value to keys that do not exist,
   which means you don’t have to manually check for missing keys and avoid KeyError.

dict в якого є дефолтні значення
'''

from collections import defaultdict


def totalFruit(fruits: List[int]) -> int:
    begin = 0
    result = 0
    window_state = defaultdict(int)

    for end in range(len(fruits)):
        window_state[fruits[end]] += 1

        while len(window_state) > 2:
            window_state[fruits[begin]] -= 1
            if window_state[fruits[begin]] == 0:
                del window_state[fruits[begin]]
            
            begin += 1
        
        result = max(result, end - begin + 1)

    return result

