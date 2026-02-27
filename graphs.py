'''
Graphs


є в графа node/вершина(vertex)
            ребра(edges)

граф може бути directed, undirected. Циклічний, не циклічний

connected components (компоненти зв'язаності), типу як острова держави.

в directed графа є Indegree/Outdegree. скільки заходить в ноду і скільки виходить з ноди, in/out
в undirected in == out

в кожної ноди є значення і може бути сусіди.

Node:
    Value
    Neightbors []*Node

    
Обхід грава за DFS або BFS

O(V + E)

dfs: (stack)
    seen = {}
    stack = [D] # D нехай буде початок, нода з якої стартуєм
    while stack:
        v <- stack.pop
        seen?
        stack <- v.ngbhs

в стрек зберігаються тільки вершини

BFS: (queue)
    q <- A
    seen
    while q:
        v <- q.popleft
        v.ngbhs -> q.end

        


найкоротший шлях це bfs


'''



'''
752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total
 number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.



Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.

тут BFS


'''
from typing import List, Optional


def openLock(deadends: List[str], target: str) -> int:
    pass





# ================================================================================================================




'''
433. Minimum Genetic Mutation



'''


# ================================================================================================================


'''
994. Rotting Oranges



'''


# ================================================================================================================




'''
2101. Detonate the maximum bombs



'''


# ================================================================================================================


'''
841. Keys and rooms


There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
 Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, 
and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms,
 or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.


Constraints:

n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.


граф тут заданий у вигляді Adjacency List, список суміжності, індекс в масиві це і є вершина.

          0.  1.  2.  3
rooms = [[1],[2],[3],[]]
0,1,2,3 зверху, це вершини графа, 0 зв'язаний з 1, 1 з 2, 2 з 3.


len(rooms) кількість кімнат відома

щоб зрозуміти, що я не всі відвідам, будем юзати seen

і якщо len(seen) співпаде з len(rooms), означає що всі кімнати ми відвідали

'''


# рекурсивно
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    def traverse(room):
        for neighbor in rooms[room]:
            if neighbor not in seen:
                seen.add(neighbor)
                traverse(neighbor)
    
    seen = {0}
    traverse(0)
    return len(seen) == len(rooms)



# ітеративно
def canVisitAllRooms2(rooms: List[List[int]]) -> bool:
    seen = {0}
    stack = [0]

    while stack:
        room = stack.pop()

        for neighbor in rooms[room]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return len(seen) == len(rooms)

 


# ================================================================================================================


'''
1971. Find if path exists in graph


There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between
 vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, 
or false otherwise.



тобто є ребро між 0 та 1, між 1 та 2, між 2 та 0

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

[0,1],[1,2],[2,0] - це нам треба розпарсити, а потім зробити dfs/bfs


Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.


bi-directional - двонапрамлений, назад і вперед від вершини до вершини.


edges[i] = [ui, vi] u - із, v - в



graph це буде хеш мапа, в якої ключ це вершина, а значення це список значень



'''
from collections import defaultdict


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    seen = set()
    seen.add(source)
    stack = [source]

    while stack:
        v = stack.pop()

        if v == destination:
            return True

        for neighbor in graph[v]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)

    return False

    
# ================================================================================================================


'''
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, 
the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of 
a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).




'''



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    pass
        