'''
Binary Tree



DFS - пошук в глибину. Depth First Search


дерево це такий випадок графа

коли пишемо рекурсивний алготирм, завжди треба продумати базовий випадок, щоб не була вічна рекурсія.

перша нода в дереві називається root.

Дерево росте зверху вниз.

В кожної ноди є значення, показник на ліву нижню ноду та показник на праву нижню ноду.

Останні ноди, це ноди в яких немає потомків, дітей, наступних нод. Називаються листочки leaves, leaf



в DFS спочатку ниряєм в глибину.

тобто з root ниряю найнижче по гілці як тільки можу, не знайли вертаємось в root, і в настпну гілку ниряєм 



def dfs(node):
    if not node:
        return

    (pre-order)

    dfs(node.left)

    (in-order)
    
    dfs(node.right)

    (post-order)

    return

    

Коли я працюю зі значенням до того, як я зроблю рекурсивнні виклики, це називається pre-order.

Коли між двома рекурсивними викликами, in-order.

Коли після рекурсивних викликів, post-order.

'''




'''
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth 
is the number of nodes along the longest path from the root node down to the farthest leaf node.


Input: root = [3,9,20,null,null,15,7]
Output: 3



повернути максимальну глибину дерева
'''


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# рекурсивно
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right) + 1



# ітеративно
def maxDepth2(root: Optional[TreeNode]) -> int:
    stack = [(root, 1)]
    result = 0

    while stack:
        node, depth = stack.pop()
        if not node:
            continue

        result = max(result, depth)
        stack.append((node.left, depth + 1))
        stack.append((node.right, depth + 1))
    
    return result



# ==========================================================================================



'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.


'''


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return 
    
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root


# ==========================================================================================


'''
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

піддерева розглядаєм, як окремі дерева
робим ітеративний dfs, куди кладемо зразу зліва піддерево і справа піддерево.

'''


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    
    stack = [root.left, root.right]

    while stack:
        right = stack.pop()
        left = stack.pop()

        if not left and not right:
            continue

        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        stack.append(left.left)
        stack.append(right.right)
        stack.append(right.left)
        stack.append(left.right)
    return True
    


# ==========================================================================================


'''
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree 
has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

важливо що від корня до листочка!

можна ітеративно і рекурсивно
'''

# ітеративно
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    stack = [(root, 0)]

    while stack:
        node, current_sum = stack.pop()
        if not node:
            continue
        
        current_sum += node.val

        if not node.left and not node.right and current_sum == targetSum:
            return True
        
        stack.append((node.left, current_sum))
        stack.append((node.right, current_sum))
    
    return False