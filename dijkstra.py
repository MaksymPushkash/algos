'''
Dijkstra (Пошук найкоротшого шляху в зваженому графі)

зважений граф, коли наприклад від ноди до ноди є якась відстань

шлях накопичуємі

дейкстра не працює з відємними значеннями!

псевдокод:


distances = {}
min_heap <- (0, start)
distances[start] = 0

while min_heap:
    current_distance, node <- min_heap
    if current_distance > distance[node]:
        continue
    
    for neighbor, distance_to_neighbor in graph[node]:
        new_distance = current_distance + distance_to_neighbor

        if new_distance < distance[neighbor]:
            distance[node]
            min_heap[(new_distance, neighbor)]

'''






'''
743. Network delay time


You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges 
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel 
from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.



Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

'''
from typing import List
from collections import defaultdict
import heapq


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)

    for a, b, w in times:
        graph[a].append((b, w))
    
    min_heap = [(0, k)]

    distances = {}

    distances[k] = 0


    while min_heap:
        dst, node = heapq.heappop(min_heap)

        if dst > distances.get(node, float('inf')):
            continue
        
        for ngh, dst_to_ngh in graph[node]:
            new_dst = dst + dst_to_ngh
            if new_dst <  distances.get(ngh, float('inf')):
                distances[ngh] = new_dst
                heapq.heappush(min_heap, (new_dst, ngh))

    if n != len(distances):
        return -1
    
    return distances[max(distances, key = lambda x: distances[x])] # ключ в якого максимальне значення



# ==============================================================================================================================


'''
1514. Path with maximum probability

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] 
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.


Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.

'''


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    graph = defaultdict(list)

    for i in range(len(edges)):
        a = edges[i][0]
        b = edges[i][1]
        p = succProb[i]

        # якщо граф ненаправлений, то робимо в дві сторони
        graph[a].append((b, p))
        graph[b].append((a, p))


    max_heap = [(-1.0, start_node)]
    probs = {}
    probs[start_node] = 1

    while max_heap:
        p, node = heapq.heappop(max_heap)

        if node == end_node:
            return -p

        for ngh, p_to_ngh in graph[node]:
            new_prob = p_to_ngh * -p

            if ngh not in probs or new_prob > probs[ngh]:
                probs[ngh] = new_prob
                heapq.heappush(max_heap, (-new_prob, ngh))
                
    return 0


# ==============================================================================================================================


'''
787. 

There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to 
city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.

Constraints:

2 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst


одна зупинка це 3 вершини, 2 ребра

залишимо від дейкстри жадну частину(щоб від в хіпу клав мінімальну вагу), але якщо він жадно в хіпу набрав більше зупинок чим ми можемо позволити, то ми ці варіанти відсікаємо
але порівнюєм як ми попали в ноду не по ціні, а по кількості зупинок

'''


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)

    for a, b, c in flights:
        graph[a].append((b, c))

    stops = {}
    min_heap = [(0, 0, src)]
    
    while min_heap:
        cost, depth, flight = heapq.heappop(min_heap)

        if depth > k + 1:
            continue

        if flight == dst:
            return cost
        
        stops[flight] = depth

        for ngh, cost_to_ngh in graph[flight]:
            if ngh not in stops or depth + 1 <= stops[ngh]:
                heapq.heappush(min_heap, (cost + cost_to_ngh, depth + 1, ngh))

    return -1


# ==============================================================================================================================


'''


'''