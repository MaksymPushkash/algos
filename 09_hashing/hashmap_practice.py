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



є мехназм open addressing
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


class MyHashMap:
    def __init__(self):
        pass

    def put(self, key: int, value: int) -> None:
        pass
        

    def get(self, key: int) -> int:
        pass
        

    def remove(self, key: int) -> None:
        pass
        

