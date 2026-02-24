# Implementing a stack is trivial using a dynamic array
# (which we implemented earlier).
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()


'''
SUGGESTED PROBLEMS

https://leetcode.com/problems/baseball-game/

https://leetcode.com/problems/valid-parentheses/

https://leetcode.com/problems/min-stack/
'''

