'''
перший випадок

один pointer(укажчик) ми ставимо на початку, інший в кінці.

нарпиклад є в нас стрінга "abcde" і ми хочемо її реверснути.
перший покажчик на a, другий на e.
спочатку ми міняємо місцями перший та останній елемент, получається "ebcda"
і потім ми рухаєм перший показник в право, а другий в ліво на 1 

і міняємо вже ці елементи між собою, і виходить "edcba".
два показники зустрічаються один з одним і ми робимо terminate.




Загальна ідея. Ставимо два показники в колекції, на перший елемент та на останній. 
І рухаємо їх всторону один одного поки вони не зустінуться.


Складність O(n)

pointer може бути індекс в масиві, в рядку і тд.

'''
from typing import List


# Складність часова O(n). По пам'ять O(1), бо це масив.
# 344 Reverse String. 
def reverseString(s: List[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return



# ==========================================================================================


# 125 Valid Palindrome. 
# Слово palindrome, це слово яке одинаково читається, якщо читаємо зліва на право та з права на ліво.
# В нас два показники, на початку та в кінці, ми їх зводим в середину. На початку та в кінці, вони вказують на одинакові елементи.
# Тобто перший на останній елемент одинакові, другий та передостанній одинаокові, 
# і якщо десь два показники не сходяться то це не паліндром.

# забрати лишні символи, можна через ASCII.
# можемо вяти символ і поріняти чи він попадає в те шо нам треба.


# Лише після спеціальних символів та цифр (48–57) у таблиці йдуть латинські літери (починаючи з 65 для 'A' та 97 для 'a')


# в Python є метод, який перевіряє чи це символ чи це число.   isalnum()

'''
Початок: left=0 ('A'), right=29 ('a')
Цикл на кожній ітерації робить одну з чотирьох речей:

if not s[left].isalnum() — якщо лівий символ невалідний (кома, пробіл тощо) — просто пропускаємо його, зсуваємо left вправо
elif not s[right].isalnum() — якщо правий символ невалідний — пропускаємо його, зсуваємо right вліво
elif s[left].lower() == s[right].lower() — обидва валідні і рівні — зсуваємо обидва до центру
else — обидва валідні але не рівні — одразу return False

Коли left >= right — ми дійшли до центру і всі символи співпали — return True.
Ключова ідея: ми ніколи не порівнюємо символи доки не переконались що обидва валідні.
'''

def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left +=1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True 

# ==========================================================================================

'''
167 Two Sum 2 - Input Array is sorted (в цій задачі індексація з 1, і завжди є одна правильна відповідь)
дано масив чисел, який вже відсортований по зростанню. 
Треба знайти два числа так щоб їх сума складалась в target.

можна вирішити вложеним циклом, але складність O(n^2)


можна використати мапу, ми йдемо по масиву і складати в мапу,
 а потім перевіряти if taget - current in map?,
 якщо бачили то знайшли return, якщо не бачили то йдем далі continue.
так складність по часу буде O(n) і по пам'яті теж O(n) - це погано по пам'яті



вирішення з двома показниками.
 йдемо з початку та кінця, два показники. Порівнюємо з target на кожній ітерації, 
якщо target більше (відсортований масив тому що), 
то ми правий показник рухаєм в ліво, якщо target менше, то лівий показник в право.


target = 9
         *
[2,7,11,15]
 *

 2 + 15 = 17 > 9 не підходить.
Ставимо два показники, на початок та в кінець. І додаєм їх і порівнюєм з target.
Так як масив відсортований, 17 більше ніж наш target, то суму нам треба зменшити,
але щоб зменшити треба рухати правий показник, тому що масив відсортований за зростанням.
якщо будем рухіти лівий, то сума буде рости, якщо правий будем в ліво зсувати, то сума буде меншати.


Коли ми зрозумієм, що в масиві не було розвязку,
 коли ми зрозуміє, шо ми вже ніколи його не знайдем?
 - коли два показники зустрінуться.

складність по часу O(n), по пам'яті O(1) 

'''




def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return []


# ==========================================================================================


'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Тобто нам треба вернути три числа які не дорівнюють один одному, всі різні
та щоб їх сума була 0.

Це та сама задача, що й twoSum тільки з трьома числами 🤯


(a + b)
(a + b) + c = 0
c = -(a + b)

3+2=5
5+x=0
x = -5

Тобто треба знайти протижне до суми двох, тоді вийде сума трьох 0.


треба спочатку відсортувати масив, зараз пишу nums = sorted(nums), це як мінімум складність O(NlogN)
на співбесіді, сортуєм самі, quick sort/merge sort...


перевірка на дублікати поки що зробив просто сетом()

складність тут O(n^2)
'''


def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums) # O(NlogN)
    result = set() # сюди складаєм наші трійки
    n = len(nums)

    for i in range(n): # то саме що for i = 0; i < n; i++
        target = -nums[i] # беремо конкретне число і робимо його таргетом
        left = i + 1 # починаємо з наступного
        right = n - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.add((target, nums[left], nums[right]))
            elif current_sum > target:
                right -= 1
            else:
                left += 1
    return list(result)



def threeSum2(nums: list[int]):
    # sorting
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1

    result = set()

    for i in range(len(nums)):
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.add((-target, nums[left], nums[right]))
                left += 1
                right -= 1
            elif current_sum > target:
                right -= 1
            else:
                left += 1
    return list(result)


# ==========================================================================================


'''
977. Squares of a sorted array


використовуєм два показники, і заповнюєм результат з кінця.
відємні числа можуть стати найбільшими в масиві після квадрата, тому можуть стати в кінці масиву
тому масив результату нам треба заповнювати не з початку, а з кінця


  * 
[-4,-1,0,3,10]
            *
16      100 більше з правого, 

якщо більштй правий показник рухаємо правий показник вліво
і якшо більший лівий показник, рухаєм його вправо
[,100]

йдем задом на перед



abs()
у Python — це вбудована функція, яка повертає абсолютне значення (модуль) числа, 
тобто перетворює від'ємне число на додатне, зберігаючи додатні числа без змін.
'''


def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n # нам потрібен масив розміром n

    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1): # в python це йти задом на перед, len(nums) з останнього до початку 0 включно, -1 step
        if abs(nums[left]) < abs(nums[right]):
            result[i] = nums[right] * nums[right] # спочатку треба додати, а вже потім здвігати
            right -= 1
        else:
            result[i] = nums[left] * nums[left]
            left += 1

    return result



# ==========================================================================================

'''

ДЗ - DONE

11. Container with most water

два максимума не факт що правильно

[9,0,8,4,0,0,0,0,0,0,0,0,4]

між 9 та 8 поміститься 8 води

а між 4 та 4 поміститься 32 води, в кожен 0 там 4


на кожній ітерації ми робимо result = max(result, .......something)
тобто на кожній ітерації зберігаєм проміжний результат
ширина рахується тут так width = right - left
але якщо один вище іншого, води залізе як менший по висоті, min height

а якщо одна зі сторін вище за іншу, який показник рухати, де менша стіна чи більша, там де менша сторона.


'''


def maxArea(height: List[int]) -> int:
    n = len(height)
    left = 0
    right = n - 1
    area = 0

    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        area = max(area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area



# ==========================================================================================
# ==========================================================================================
# ==========================================================================================
# ==========================================================================================


'''
Це був один випадок two pointers.
Коли ми ставили два показники спочатку та вкінці та йшли на зустріч один одному.




Тут ми будемо ставити два показники на початку і будемо рухати спочатку перший і другий вслід за ним,
по якомусь принципом, чи один буде рухатись а іншій буде його доганяти, чи один робить 2 кроки інший робить 1 крок,
і те саме з іншої сторони, з кінця
Тобто починуються з одного місця і рухаються

наприклад, забрати дублікати!

буде зустрічатись в linked lists

'''


'''
26. Remove Duplicates from sorted array


[1,1,1,2,2,3,3,4,5]

має бути 1,2,3,4,5

поставили два показники на початок, на першу 1

можна рухати один з показників поки вони не будуть різними
і коли не співпадають, ми записуєм значення першого, і потім рухаєм перший до другого, вони співпадають,
 рухаєм другий поки вони не будуть різними

 один показник який йде першим, постійно рухається, він з постійною швидкістю рухається
 тому для цього показника можна просто написати for i in range(len(nums))
 а для іншого показника, базового, k=0

'''


def removeDuplicates(nums: List[int]) -> int:
    k = 0
    for i in range(len(nums)):
        # Як тільки вони перестали бути рівними
        if nums[k] != nums[i]: #якщо те що лежить під нижнім показником != там де ми знаходимся.
            k += 1 
            nums[k] = nums[i]
    return k + 1


# ==========================================================================================


'''
283. Move Zeroes


Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]



'''


def moveZeroes(nums: List[int]) -> None:
    k = 0 # перший показник, базовий
    for i in range(len(nums)): # i другий показник
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k] 
            k += 1




# ==========================================================================================
# ==========================================================================================
# ==========================================================================================
# ==========================================================================================


'''
Наступний випадок


дві колекції є
і ми один показник ставимо на одну колекцію, а другий на іншу колекцію, робимо якусь операцію, і рухаємо або той або той, або зразу два

в першому випадку ми ставили один показник на початок, другий на кінець колекції.
в другоиу випадку ми ставили два показники на початок, або кінець.
в цьому третьому випадку в нас є n-колекції, і на кожну колекцію ми ставимо по показнику.



наприклад, нам треба знайти під послідовність.

abbdefghkpy
behy під послідовність

я ставлю два показники на початок, і дивлюсь чи вони співпадають, якщо ні рухаю далі верхній показник, якщо співпадають рухаю нижній до верхнього
і як тільки закінчиться перша послідовність, верхня, то ми поченемо перевіряти умову нижньої, чи ми там все знайшли чи ні
тому по факту складність залежить тільки від верхньої колекції
'''






'''
392. Is Subsequence

'''

def isSubsequence(sub: str, s: str) -> bool:
    p1 = 0
    p2 = 0

    while p1 < len(sub) and p2 < len(s):
        if sub[p1] == s[p2]:
            p1 += 1
        p2 += 1

    return p1 == len(sub)

# ==========================================================================================


'''

ДЗ - DONE

844. Backspace String Compare


Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


тут коли решітка, то це delete

тобто я є ab#c
спочатку a, потім ввожу b, решітка - видалив b, і ввів с. Виходить ac
'''


def backspaceCompare(s: str, t: str) -> bool:
    n = len(s) - 1
    m = len(t) - 1
    skip_s = 0
    skip_t = 0

    while n >= 0 or m >= 0:
        while n >= 0:
            if s[n] == "#":
                n -= 1
                skip_s += 1
            elif skip_s > 0:
                n -= 1
                skip_s -= 1
            else:
                break
                
        while m >= 0:
            if t[m] == "#":
                m -= 1
                skip_t += 1
            elif skip_t > 0:
                m -= 1
                skip_t -= 1
            else:
                break

        if n >= 0 and m >= 0:
            if s[n] != s[m]:
                return False
        elif n >= 0 or m >= 0:
            return False

        n -= 1
        m -= 1

    return n == m




# ==========================================================================================


'''
88. Merge sorted array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1.
 The 0 is only there to ensure the merge result can fit in nums1.

 


 з двома показниками, складність буде O(n + m)
'''



def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    result = []
    p1 = 0
    p2 = 0

    while p1 < m and p2 < n:
        if nums1[p1] < nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
        else:
            result.append(nums2[p2])
            p2 += 1

    for k in range(p1, m):
        result.append(nums1[k])
    
    for k in range(p2, n):
        result.append(nums2[k])

    for i in range(len(result)):
        nums1[i] = result[i]
    return


# навпаки
def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    result = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[result] = nums1[p1]
            p1 -= 1
        else:
            nums1[result] = nums2[p2]
            p2 -= 1
        
        result -= 1
    
    while p2 >= 0:
        nums1[result] = nums2[p2]
        p2 -= 1
        result -= 1
        
        
        
        
        
        