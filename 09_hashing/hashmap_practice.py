'''
HashMap

Хеш таблиці

dict в python
map в java...

це така колекція даних, яка зберігає в собі ключ: значення

1: "a",
2: "b"...


Один із головних компонентів хеш таблиці це є хеш функція.

Наприклад масив в памяті розполіється таким цільним куском послідовним. Хеш таблиця виглядає по іншому.


В хеш таблицях є поняття бакети

є механізм chaining, не найліпший підхід

bucket(linked lists) це там де зберігаються ці ключ значення.
І яку пару ключа та значення положити в бакет і якраз ось це рішення приймає хеш функція.
Хеш функція повинна максимально старатись зменшити кількість колізій і рівномірно розподіляти дані по бакетам.


Якщо в нас погана хеш функція, ми получаємо колізії, це значить що в один бакет накопилось дуже багато елементів.



є механізм open addressing
він наприклад йде в бакет 0, бачить що вже цей бакет забитий, і йде перевіряти наступний




в хеш таблиці є ще такеий параметр Load Factor, говорить нам що вже все погано,
 бакети вже забиті, дуже багато колізій, вже операції дорогі треба шось придумати
'''



'''
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap.
 If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


'''


class Node:
    def __init__(self, key: int, value: int, next_node=None) -> None:
        self.key = key
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def get(self, key: int) -> int:
        current = self.head

        while current is not None:
            if current.key == key:
                return current.value
            
            current = current.next
        
        return -1

    def put(self, key: int, value: int) -> None:
        current = self.head

        while current is not None:
            if current.key == key:
                current.value = value
                return
            
            current = current.next
        
        new_node = Node(key, value, self.head)
        self.head = new_node
    
    def remove(self, key: int) -> None:
        if self.head is None:
            return
        
        if self.head.key == key:
            self.head = self.head.next
            return
        
        current = self.head

        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
                return
            
            current = current.next


class MyHashMap:
    def __init__(self) -> None:
        self.n = 991
        self.buckets = [LinkedList() for _ in range(self.n)]
    
    def hash(self, key: int) -> int:
        return key % self.n


    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        self.buckets[index].put(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        return self.buckets[index].get(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        self.buckets[index].remove(key)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)