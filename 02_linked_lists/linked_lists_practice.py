'''
Linked List
Зв'язаний список


це набір вузлів(нод), які мають в собі якісь дані і зв'язані один з одним в ципочку.



наприклад в нас є якась нода, в неї є якесь значення та посилання на наступну ноду. І так само наступна.
І в кінці остання ні нащо не вказує.

Початок linked lista називають head, а кінець tail.

Node
    - value int
    - next *Node



Яка різниця між Linked List та Array?
    Масив в пам'яті зберігається послідовним куском, і тому індексуватись по ньому ми можем за константу O(1).
    В нас якби є початок масиву, ми знаєм розмір кожної комірки і тому получити якусь там 4 комірку можем
    за константний час простою арифметикою.
    У випадку з зв'язаними списками, це не так. Тобто ніхто не гарантує, що нульова нода знаходиться прямо
    перед першою нодою. Вони можуть бути абсолютно розкидані по пам'яті. І можемо від однієї ноди до
    іншої переходити тільки по показнику де вона знаходиться.

    
Зазвичай в задачах на linked lists нам дано тільки head.
А потім від голови нас просять розкрутити інші операції. Наприклад пошук.



Наприклад, знайди ноду n2 і верни її значення. І при цьому в нас є тільки показник на head.
Ми можемо від голови піти до наступної ноди від неї в наступну і ось ми прийшли і потім в неї ми вернемо значення.

В нас є якийсь ітератор.
назвемо його current і він буде рівний head, current = this.head.
а потім переходимо до наступної ноди, current = current.next.
Ось так ми ітеруємось по зв'язаному списку.

current = this.head
for i = 0; i < index; i++
    current = current.next
current.value




Наприклад я хочу змінити head. O(1)

new_node(7)
new_node.next = this.head
this.head = new_node



Наприклад я хочу вставити елемент в середину звязаного списка.

old_next = current.next
current.next = new_node
new_node.next = old_node




Наприклад я хочу видалити елемент в середині списку

current.next = current.next.next





Python does not have a built-in or "native" linked list data type in its standard library.
However, linked lists can be implemented in Python in a few ways:

Using collections.deque

The collections.deque class from the standard library is implemented internally 
as a doubly-linked list of blocks and is a good choice for implementing queues or stacks. 

Pros:
Provides constant O(1) time complexity for appending and popping elements 
from both ends (the beginning and the end of the list).
It is a built-in, highly optimized class within the standard library.

Cons:
Does not offer O(1) insertion or deletion of elements in the middle of the list by index or value.
You cannot directly access the underlying node objects or pointers


'''




'''
707. Design Linked list


Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next.
 val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to 
indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list.
 After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
 If index equals the length of the linked list, the node will be appended to the end of the linked list. 
 If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

'''



class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.length = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        current = self.left.next
        
        for _ in range(index):
            current = current.next
            
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        
        next_node = self.left.next
        prev_node = self.left
        
        new_node.next = next_node
        new_node.prev = prev_node
        
        prev_node.next = new_node
        next_node.prev = new_node
        
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        
        next_node = self.right
        prev_node = self.right.prev
        
        new_node.next = next_node
        new_node.prev = prev_node
        
        prev_node.next = new_node
        next_node.prev = new_node
        
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
            
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.length:
            self.addAtTail(val)
            return
            
        current = self.left.next

        for _ in range(index):
            current = current.next
            
        new_node = Node(val)
        next_node = current
        prev_node = current.prev
        
        new_node.next = next_node
        new_node.prev = prev_node
        
        prev_node.next = new_node
        next_node.prev = new_node
        
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
            
        current = self.left.next

        for _ in range(index):
            current = current.next
            
        prev_node = current.prev
        next_node = current.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.length -= 1



# ==========================================================================================




'''
876. Middle of the Linked List (single linked list)


Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.



Підхід Fast and Slow Pointer

В нас буде два pointers, один швидкий, інший повільний.
якщо кількість непарна:
Тобто, fast = fast.next.next
       slow = slow.next

якщо кількість парна:
останній елемент має некст просто він вказує в нікуда, тому він зможу пройти далі, і slow також пройде надругий центральний елемент.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


# ==========================================================================================


'''
2095. Delete the middle node of a linked list


You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.


нода сама себе видалити не може

щоб видалити ноду, треба стояти на мунилій ноді, і наступну тоді можна буде видалити.

будемо робити те саме що й в минулій задачі, тільки один pointer будем йому типу давати фору
'''


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None

    slow = head
    fast = head.next.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    slow.next = slow.next.next # видаляєм ноду
    return head


# ==========================================================================================


'''
206. Reverse Linked list

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

'''

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

    return prev


# ==========================================================================================


'''
234. Palindrome Linked List


Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

'''


def isPalindrome(head: Optional[ListNode]) -> bool:
    def middle(head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(head):
        prev = None
        current = head

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev
    
    mid = middle(head)
    second = reverse(mid)

    first = head

    while first and second:
        if first.val != second.val:
            return False
        
        first = first.next
        second = second.next
        
    return True


# ==========================================================================================


'''
83. Remove Duplicates from sorted list

Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. Return the linked list sorted as well.

    *   
[1, 1, 2]

'''



def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head

    while current and current.next:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next

    return head



# ==========================================================================================



'''
19. Remove Nth Node from  end of the list

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

треба видалити нну ноду з кінця




використовуємо pointers, одному даєм фору в n кроків, вони зберігають цю відстань між собою постійно


і робимо заглушку, яка буде вказувати на першу ноду


тобто коли перший дойде до кінця, другий pointer буде за n кроків там де нам треба
'''


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head # заглушка на першу ноду

    first = dummy
    second = dummy

    for i in range(n + 1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next



# ==========================================================================================


'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Input: head = [1,2,3,4]
Output: [2,1,4,3]



'''


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head

    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        
        first.next = second.next
        second.next = first
        current.next = second

        current = first
    return dummy.next


# ==========================================================================================


'''
21. Merge two sorted lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


'''


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    p1 = list1
    p2 = list2

    while p1 and p2:
        if p1.val < p2.val:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        
        current = current.next

    if p1:
        current.next = p1
    elif p2:
        current.next = p2

    return dummy.next


# ==========================================================================================


'''
141. Linked list cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


Є алгоритм Флойда.


'''


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
            
    return False