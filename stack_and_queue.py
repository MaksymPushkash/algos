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


'''