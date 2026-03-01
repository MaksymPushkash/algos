'''
Backtracking


перебор з поверненням

це просто підзід до перебору

у вигляді дерева
backtracking допомагає зробити перебір всього, але при цьому завчасно відрізати не валідні для нас шляхи


використовуєм коли треба зробити якийсь перебір

'''




'''
46. Permutations


Given an array nums of distinct integers, return all the possible permutations.
 You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


якщо в мене n чисел, то перестановок буде n!


треба вернути всі можливі перестановки

'''
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(acc):
        if len(acc) == len(nums):
            result.append(acc[:])
            return
        for num in nums:
            if num not in acc:
                acc.append(num)
                backtrack(acc)
                acc.pop()

    backtrack([])
    return result



# =====================================================================================================================================


'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
 

'''



def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def backtrack(acc, start):
        if len(acc) == k:
            result.append(acc[:])
            return

        for num in range(start, n + 1):
            acc.append(num)
            backtrack(acc, num + 1)
            acc.pop()

    backtrack([], 1)
    return result



# =====================================================================================================================================


'''
78. Subsets


Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


'''


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)

    def backtrack(acc, start):
        if start > n:
            return

        result.append(acc[:])

        for i in range(start, n):
            acc.append(nums[i])
            backtrack(acc, i + 1)
            acc.pop()

    backtrack([], 0)
    return result




# =====================================================================================================================================



'''
22. Generate Parentheses


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
 


'''



def generateParenthesis(n: int) -> List[str]:
    result = []

    def backtrack(acc, op, cl): # open, closed
        if len(acc) == 2*n:
            result.append(acc)
            return

        if op < n:
            backtrack(acc + "(", op + 1, cl)
        if cl < op:
            backtrack(acc + ")", op, cl + 1)


    backtrack("", 0, 0)

    return result



# =====================================================================================================================================



'''
216. Combination Sum 3


Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:

2 <= k <= 9
1 <= n <= 60


'''


def combinationSum3(k: int, n: int) -> List[List[int]]:
    result = []

    def backtrack(start, acc, path_sum):
        if len(acc) == k:
            if path_sum == n:
                result.append(acc[:])
            return

        if path_sum > n:
            return

        for num in range(start, 10):
            acc.append(num)
            backtrack(num + 1, acc, path_sum + num)
            acc.pop()

    backtrack(1, [], 0)
    return result



# =====================================================================================================================================


'''
17. Letter Combinations of a phone number


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

'''


def letterCombinations(digits: str) -> List[str]:
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []

    if not digits:
        return result


    def backtrack(pos, word):
        if len(word) == len(digits):
            result.append(word)
            return

        for letter in keyboard[digits[pos]]:
            backtrack(pos + 1, word + letter)


    backtrack(0, "")
    return result



# =====================================================================================================================================


'''
51. N-Queens



The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space,
 respectively.

 

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

'''




def solveNQueens(n: int) -> List[List[str]]:
    result = []

    def backtrack(row, columns, diagonals, t_diagonals, board):
        if row == n:
            result.append(["".join(board[i]) for i in range(n)])
            return
        
        for col in range(n):
            current_diagonal = row + col
            current_t_diagonal = row - col

            if col in columns or current_diagonal in diagonals or current_t_diagonal in t_diagonals:
                continue
            
            columns.add(col)
            diagonals.add(current_diagonal)
            t_diagonals.add(current_t_diagonal)
            board[row][col] = "Q"

            backtrack(row + 1, columns, diagonals, t_diagonals, board)

            columns.remove(col)
            diagonals.remove(current_diagonal)
            t_diagonals.remove(current_t_diagonal)
            board[row][col] = "."


    board = [["."] * n for _ in  range(n)]

    backtrack(0, set(), set(), set(), board)
    return result




# =====================================================================================================================================

