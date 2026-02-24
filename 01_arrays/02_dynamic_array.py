# Python arrays are dynamic by default, but this is an example of resizing.
class Array:
    def __init__(self):
        self.capacity = 2 # скільки комірок виділено в пам'яті
        self.length = 0 # # скільки комірок реально зайнято даними
        self.arr = [0] * 2  # Array of capacity = 2

    # Insert n in the last position of the array, like arr.append(x)
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity *= 2
        newArr = [0] * self.capacity

        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1

    # Get value at i-th index
    def get(self, i):
        if i < self.length:
            return self.arr[i]
        # Here we would throw an out of bounds exception

    # Insert n at i-th index
    def insert(self, i, n):
        if i < self.length:
            self.arr[i] = n
            return
        # Here we would throw an out of bounds exception

    def print(self):
        for i in range(self.length):
            print(self.arr[i])
        print()

        

'''
SUGGESTED PROBLEMS

https://leetcode.com/problems/concatenation-of-array/


Static array не може змінити розмір. 
Dynamic array вирішує це одним трюком: коли місця немає — створити новий масив більшого розміру і перекопіювати все туди.


list в Python працює рівно так само всередині. 
Коли ти робиш arr.append(x) — це той самий pushback. 
Python сам керує capacity і resize за тебе. 
Ця реалізація в коді показує що відбувається "під капотом".

'''