'''
BFS - пошук в ширину.

Breadth First Search

ми по слоями розпоковуєм дерево

якщо нам важливі якісь зв'язки між нодами, то тоді DFS


def bfs(root):
    queue = [root]

    while queue:
        level_size = len(queue)

        fir _ in range(level_size):
            node = queue.popleft()
            queue = node.left
            queue = node.right
'''



'''
102. Binary tree level order traversal


Given the root of a binary tree, return the level order traversal of its nodes' values.
 (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

'''
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = deque[root]
    result = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        result.append(current_level)

    return result

# ======================================================================================================



'''
515. Find Largest Value in each tree row


Given the root of a binary tree,
 return an array of the largest value in each row of the tree (0-indexed).

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]


'''



def largestValues(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        level_max = float('-inf')

        for _ in range(level_size):
            node = q.popleft()
            level_max = max(level_max, node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level_max)

    return result

# ======================================================================================================


'''
199. Binary tree right side view

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.


беремо останню ноду на левелі

'''


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        current_level = []

        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        result.append(current_level[-1])
    return result

# краще
def rightSideView2(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)

        for i in range(level_size):
            node = q.popleft()

            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
    return result


# ======================================================================================================



'''
ДЗ


117. Populating next right pointers in each node 2


Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A),
 your function should populate each next pointer to point to its next right node,
   just like in Figure B. The serialized output is in level order as connected by the next pointers,
     with '#' signifying the end of each level.


дано дерево, його треба прошити, тобто весь левел ми зшиваємо між собою
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def connect(root: 'Node') -> 'Node':
    # prev?
    # node = q.popleft()
    # prev.next = node
    pass


# ======================================================================================================


'''
1325. Delete leaves with a given value

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target,
 if its parent node becomes a leaf node and has the value target, it should also be deleted 
 (you need to continue doing that until you cannot).

 leave нода без дітей, last node
 
можна вирішити DFS'ом і post order тут буде

'''

def removeLeafNodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if not root:
        return None
    
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)

    if not root.left and not root.right and root.val == target: # post order
        return None

    return root


# ======================================================================================================



'''
1302. Deeptest Leaves Sum

Given the root of a binary tree, return the sum of values of its deepest leaves.

BFS - останній поверх забираємо

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = deque[root]
    result = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        result.append(current_level)

    return result

'''


def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    q = deque([root])
    last_level = []

    while q:
        level_size = len(q)
        last_level = [] #  # overwrite each time — final value = last level

        for _ in range(level_size):
            node = q.popleft()
            last_level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
    return sum(last_level)


# ======================================================================================================


'''
543. Diameter of binary tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
 This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


діаметр дерева - найдовший шлях між двом любими нодами в дереві


D = max depth of L, R branch
'''


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diametr = 0

    def depth(node):
        if not node:
            return 0

        left = depth(node.left)
        right = depth(node.right)

        diametr = max(diametr, left + right)

        return max(left, right) + 1
    
    depth(root)
    return diametr


# ======================================================================================================


'''

ДЗ

103. Binary Tree zigzag level order traversal


Given the root of a binary tree, return the zigzag level order
 traversal of its nodes' values. (i.e., from left to right, then right to left for the next
   level and alternate between).


'''

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    pass



# ======================================================================================================

'''
236. Lowest common ancestor of a binary tree


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two
 nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to 
 be a descendant of itself).”

 

 ми хочемо знати чи в гілці підімною вернулось чи не вернулось.
 і коли ми знаходимось в якісь ноді, для якої з обох гілок вернулось, значить це вона і є
'''

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None

    if root == p or root == q:
        return root

    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root
    if l:
        return l
    if r:
        return r

    return None


# ======================================================================================================
