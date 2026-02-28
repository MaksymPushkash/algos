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



граф можна зберігати ось так: graph = defaultdict(list), де ключ це є нода, а значення цього ключа це список сусідів ноди


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
    if "0000" in deadends:
        return -1

    queue = deque([("0000", 0)])
    seen = set(deadends)

    def neighbours(current):
        result = []

        for i in range(4):
            num = int(current[i])

            for d in [-1, 1]:
                x = (num + d) % 10
                result.append(current[:i] + str(x) + current[i+1:])

        return result

    while queue:
        current, steps = queue.popleft()

        if current == target:
            return steps

        for n in neighbours(current):
            if n not in seen:
                queue.append((n, steps + 1))
                seen.add(n)

    return -1



# ================================================================================================================




'''
ДЗ


433. Minimum Genetic Mutation


A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation
 is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed
 to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

'''

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    pass




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
from collections import defaultdict, deque


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
    if not node:
        return node
    
    seen = {} # кого ми вже бачили і його є ми будем використовувати для зберігання копій
    stack = [node] # положили ноду яка нам прийшла в стек
    seen[node] = Node(node.val, []) # в seen ось ця [нода], вона рівна вже новій ноді но з таким же значенням

    while stack:
        v = stack.pop()
        for n in v.neighbors:
            if n not in seen:
                seen[n] = Node(n.val, []) # тут створюю її копію
                stack.append(n)
            
            seen[v].neighbors.append(seen[n]) # тут цей звязок між нодами я встановлюю в копії



    return seen[node]



# ================================================================================================================


'''
1557. Minimum Number of Vertices to reach add nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] 
represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.


Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]. другий елемент це кількість входів в ноду
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5].
 From 3 we can reach [3,4,2,5]. So we output [0,3].


Constraints:

2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.


Треба знайли мінімальну кількість вершин з яких ми можемо обійти весь граф.


якщо в них немає ходів вони автоматично мають бути у відповіді

якщо в ноди Indegree > 0 значить якось в неї можна прийти
якщо в ноди indegree = 0 значить в неї ніяк не можна прийти, значить з неї і треба починати

'''


def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    in_degree = [0] * n

    for _, to in edges:
        in_degree[to] += 1
    
    return [node for node in range(n) if in_degree[node] == 0]



# ================================================================================================================


'''
547. Number of provinces


There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

'''


def findCircleNum(isConnected: List[List[int]]) -> int:
    graph = defaultdict(list)
    n = len(isConnected)

    # проходимось по матриці
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j]:
                graph[i].append(j)
                graph[j].append(i)
    
    seen = set()
    number = 0

    for i in range(n):
        if i not in seen:
            number += 1
            seen.add(i)
    
            queue = deque([i])

            while queue:
                v = queue.popleft()
                for n in graph[v]:
                    if n not in seen:
                        seen.add(n)
                        queue.append(n)
    
    return number



# ================================================================================================================


'''
200. Number of islands


Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


'''




def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    number = 0
    n = len(grid)
    m = len(grid[0])

    def is_not_valid(r, c):
        return r < 0 or c < 0 or r >= n or c >= m or grid[r][c] != '1'


    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                number += 1

                queue = deque([(i, j)])

                while queue:
                    r, c = queue.popleft() # row, column
                    if not is_not_valid(r, c):
                        grid[r][c] = '0'
                        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                            queue.append((r+dx, c+dy)) 

    return number


# ================================================================================================================


'''
1466. Reorder Routes to make all paths lead to the city zero


There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between 
two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one 
direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.




Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).


Constraints:

2 <= n <= 5 * 104
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi


ми запам'ятовуєм в кожного ребра його оригінальне направлення, а потім граф конвертуєм в ненаправлений(bi-directional) 
і якщо це ребро було він 0, то ми йогго перевртаєм.


'''



def minReorder(n: int, connections: List[List[int]]) -> int:
    og_directions = set()
    graph = defaultdict(list)

    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
        og_directions.add((a, b))
    
    turns = 0
    seen = {0}
    stack = [0]

    while stack:
        v = stack.pop()

        for n in graph[v]:
            if n not in seen:
                if (v, n) in og_directions:
                    turns += 1

                stack.append(n)
                seen.add(n)

    return turns



# ================================================================================================================



'''
ДЗ. 15'th video 42:00

695. Max Area of Island


You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

вирішується як задача Number Of Islands

'''


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    pass






# ================================================================================================================


'''
2368.  Reachable nodes with restrictions


There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted
 which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.


Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4
Explanation: The diagram above shows the tree.
We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.



Constraints:

2 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
1 <= restricted.length < n
1 <= restricted[i] < n
All the values of restricted are unique.


скільки нод ми можемо відвідати, не трогаючи заборонені ноди


'''



def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    seen = set(restricted)
    seen.add(0)
    result = 0

    stack = [0]

    while stack:
        v = stack.pop()
        result += 1

        for n in graph[v]:
            if n not in seen:
                seen.add(n)
                stack.append(n)

    return result


# ================================================================================================================


'''
542. 01 Matrix


Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Ex1:
Input: mat = [[0,0,0],
              [0,1,0],
              [0,0,0]]

Output: [[0,0,0],[0,1,0],[0,0,0]]

Ex2:
Input: mat = [[0,0,0],
              [0,1,0],
              [1,1,1]]

Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
 

Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/


треба повернути відстань до найближчого нуля для кожної клітки



з самого початку ми пройдемось по всій матриці і додамо в queue всі позиції нулів.
тобто наша queue перед початком bfs буде вже складатися з нулів
тоді кожен bfs почне по черзі розростатись на застріч один одного
а якщо один bfs цю точку вже помітив, він до неї був ближче
візуальні це ніби паралельно, але код не паралельний


ви від кожного нуля по суті запускаєм bfs, і якшо ми попали в якусь клітинку а вона вже visited, значить вона вже була частиною іншого bfs, який до неї ближче



'''


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    if not mat:
        return mat
    
    n = len(mat)
    m = len(mat[0])

    seen = set()

    def is_not_valid(r, c):
        return r < 0 or c < 0 or r >= n or c >= m or (r, c) in seen

    queue = deque([])

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                queue.append((i, j, 1))
                seen.add((i, j))
    
    while queue:
        r, c, d = queue.popleft()

        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            if not is_not_valid(r+dx, c+dy): 
                mat[r+dx][c+dy] = d
                queue.append((r+dx, c+dy, d+1))
                seen.add((r+dx, c+dy))
    
    return mat



# ================================================================================================================



'''
ДЗ


994. Rotting Oranges


You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:


Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:


Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

'''


def orangesRotting(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    fresh_counts = 0
    minutes = 0

    queue = deque([])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh_counts += 1
            if grid[i][j] == 2:
                queue.append((i, j, minutes))
    
    while queue:
        i, j, minutes = queue.popleft()

        for di, dj, in [(0,1), (1,0), (-1,0), (0,-1)]:
            new_i = i + di
            new_j = j + dj

            if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                fresh_counts -= 1
                grid[new_i][new_j] = 2
                queue.append((new_i, new_j, minutes + 1))

    if fresh_counts == 0:
        return minutes
    else:
        return -1



# ================================================================================================================




'''
ДЗ


1129. Shortest path with alternating colors


You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1.
 Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x 
Example 1:



Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < nsuch that the edge colors alternate along the path, or -1 if such a path does not exist.





'''

def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    RED = 0
    BLUE = 1

    graph = defaultdict(lambda: defaultdict(list)) # вийде мапа і мапа яка дає список, {}{} -> []

    for a, b in redEdges:
        graph[RED][a].append(b)
    
    for a, b in blueEdges:
        graph[BLUE][a].append(b)
    
    result = [float('inf')] * n
    result[0] = 0

    queue = deque([(0, RED, 0), (0, BLUE, 0)])
    seen = {(0, RED), (0, BLUE)}

    while queue:
        v, color, depth = queue.popleft()
        result[v] = min(result[v], depth)

        for n in graph[color][v]:
            if (n, 1 - color) not in seen:
                seen.add((n, 1 - color))
                queue.append((n, 1 - color), depth + 1)


    return [x if x != float('inf') else -1 for x in result]




# ================================================================================================================



'''
1926. 


You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell
 you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze.
 Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze.
   The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.


'''



def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    rows = len(maze)
    cols = len(maze[0])

    e_r, e_c = entrance # entrance_row, entrance_column

    maze[e_r][e_c] = "+"

    queue = deque([(e_r, e_c, 0)])

    while queue:
        r, c, num = queue.popleft()

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_r = r + dr
            new_c = c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and maze[new_r][new_c] == ".":
                if new_r == 0 or new_r == rows - 1 or new_c == 0 or new_c == cols - 1:
                    return num + 1

                queue.append((new_r, new_c, num + 1))
                maze[new_r][new_c] = "+"
    
    return -1



# ================================================================================================================



'''
1091. Shortest Path in binary matrix


Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

'''


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1:
        return -1

    grid[0][0] = 1

    queue = deque([(0, 0, 1)])

    while queue:
        r, c, num = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return num

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
            new_r = r + dr
            new_c = c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 0:
                if new_r == rows - 1 and new_c == cols - 1:
                    return num + 1

                queue.append((new_r, new_c, num + 1))
                grid[new_r][new_c] = 1
    
    return -1



# ================================================================================================================




'''




'''