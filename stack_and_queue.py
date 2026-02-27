'''
Stack/Queue




Stack - Last In First Out. LIFO. Останній прийшов, перший пішов. Можемо реалізувати на масиві, 
або на single linked list.
ми додаєм в голову linked list і забираєм з голови linked list. Додати в стек, забрати зі стрек O(1).


Queque - First In First Out. FIFO. Можна реалізувати на doubly linked list.
Коли елемент приходить в чергу він приходить в кінець, коли елемент забираємо, забираємо з початку черги.
Операції O(1).

'''


'''
20. Valid Parenthess

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

'''


def isValid(s: str) -> bool:
    pair = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    stack = []

    for c in s:
        if c in pair:
            stack.append(c)
        else:
            if not stack:
                return False
            
            prev = stack.pop()
            if c != pair[prev]:
                return False
                
    return len(stack) == 0


# ==========================================================================================


'''
1047. Remove All Adjacent Duplicates in string

You are given a string s consisting of lowercase English letters.
 A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
 It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the 
letters are adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"

забрати всі сусідні дублікати в рядку


будемо проходитись по рядку, все що зустрінем будем перевіряти з тим що лежить в стеку.

наприклад, перше йде a, стеку поки нічого, добавляєм, потім b, добавляєм, потім знову b, в стеку є, видаляєм b зі стеку,
потім знову a, а є в стек, видаляєм зі стеку, ну і потім с а, добавляєм, і виходить ca
'''



def removeDuplicates(s: str) -> str:
    stack = []
    # якщо true and true то піде далі
    for c in s:
        if stack and c == stack[-1]: # верхній елемент стека | як працює and тобто якщо stack false то в c == stack[-1] він навіть не піде
            stack.pop() 
        else:
            stack.append(c)

    return "".join(stack)



# ==========================================================================================

'''
2390. Removing stars from a string


You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.

будемо додавати всі сиволи в стек, а коли зустрінем * будем видаляти останній елемент в стеці

'''


def removeStars(s: str) -> str:
    stack = []

    for c in s:
        if c == '*':
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)


# ==========================================================================================



'''
71. Simplify Path


You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
 Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
 For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.


нам треба ігнорувати ////////, коли .. ми робим pop


'''


def simplifyPath(path: str) -> str:
    stack = []

    for c in path.split("/"):
        if c == "" or c == ".":
            continue
        elif c == "..":
            if stack:
                stack.pop()
        else:
            stack.append(c)

    return "/" + "/".join(stack)


# ==========================================================================================


'''
933. Number of recent calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
 and returns the number of requests that has happened in the past 3000 milliseconds 
 (including the new request). Specifically, return the number of requests that have happened 
 in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


кожен пінг в нас йде з t
тут вже черга буде

наприклад приходить 3000


3002 - 3000 = 2
1 не підходить


будем використовувати deque, double ended queue можна додавати зліва appendleft() та справа append() і так само pop

можна ще реалізувати на doubly linked list
'''

from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        window_start = t - 3000
        while self.q and self.q[0] < window_start:
            self.q.popleft()
        
        return len(self.q)
