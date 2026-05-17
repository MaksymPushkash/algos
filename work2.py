class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head

        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        self.size += 1

        if index == 0:
            new_node = Node(val, self.head)
            self.head = new_node
            return
        
        current = self.head
        for i in range(index - 1):
            current = current.next

        old_next = current.next
        current.next = Node(val, old_next)
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
            
        self.size -= 1

        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(index - 1):
            current = current.next

        current.next = current.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)