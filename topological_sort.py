'''
Topological Sort









допомагає зрозуміти чи можем досягнути до ноди

є кілька реалізацій, найчастіше використовується алгоритм кана
граф маж бути направлений і нециклічний

завадоим таблицю in degree, кількість входів в ноду
і використовуєм bfs, в bfs використовуєм queue, в чергу попадають в порядку залежності ноди.



'''

'''
207. Course Schedule


There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to 
take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.


'''
from typing import List
from collections import defaultdict, deque


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1
    
    queue = deque()
    # спочатку чергу забиваєм чимось, курс з якого ми почнем
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
    
    n = 0
    while queue:
        node = queue.popleft()
        n += 1
        
        for ngh in graph[node]:
            in_degree[ngh] -= 1
            if in_degree[ngh] == 0:
                queue.append(ngh)

    return n == numCourses

# =======================================================================================================================================


'''
210. Course Schedule 2


There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites
 where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
 If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
 So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.




'''

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1
    
    queue = deque()
    
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
    
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for ngh in graph[node]:
            in_degree[ngh] -= 1
            if in_degree[ngh] == 0:
                queue.append(ngh)

    if len(order) == numCourses:
        return order
    else:
        return []
    


# ================================================================================================================================



'''
2115. Find All possible recipes from given supplies


You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients.
 The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
 A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply
 of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".


Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.






'''



def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    graph = defaultdict(list)
    in_degree = {}

    for recipe, components in zip(recipes, ingredients):
        in_degree[recipe] = len(components)
        for component in components:
            graph[component].append(recipe)

    queue = deque(supplies)
    result = []

    while queue:
        suppply = queue.popleft()

        for recipe in graph[suppply]:
            in_degree[recipe] -= 1
            if in_degree[recipe] == 0:
                queue.append(recipe)
                result.append(recipe)

    return result
