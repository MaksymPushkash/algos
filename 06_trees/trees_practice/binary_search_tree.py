'''
Binary Search Tree

Для кожної ноди значення зліва буде менше ніж справа і так для кожної ноди.

'''




'''
700. Search in a binary search tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.


'''
from typing import Optional
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None

    if root.val == val:
        return root
    
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


# ========================================================================================================


'''
701. Insert into Binary search tree


You are given the root node of a binary search tree (BST) and a value to insert into the tree.
 Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a
 BST after insertion. You can return any of them.




'''


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insertIntoBST(root.right, val)
    elif val < root.val:
        root.left = insertIntoBST(root.left, val)
    return root

# ========================================================================================================


'''
98. Validate binary search tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.


якщо ми зліва, то ми точно менші ніж батьківська нода
і навпаки
'''

def isValidBST(root: Optional[TreeNode]) -> bool:
    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, min_r, max_r = stack.pop()

        if not node:
            continue

        if node.val <= min_r or node.val >= max_r:
            return False
        
        stack.append((node.left, min_r, node.val))
        stack.append((node.right, node.val, max_r))
        
    return True



 # ========================================================================================================


'''
110. Balanced binary tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees 
of every node never differs by more than one.


знайдемо висоту кожного піддерева, і тоді якщо висота правого або лівого відрізняється більше чим на 1,
 то воно не збалансоване
'''


def isBalanced(root: Optional[TreeNode]) -> bool:
    def height(root):
        if not root:
            return 0
        
        return 1 + max(height(root.left), height(root.right))
    
    if not root:
        return True
    
    left_h = height(root.left)
    right_h = height(root.right)

    if abs(left_h - right_h) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)



# ========================================================================================================



