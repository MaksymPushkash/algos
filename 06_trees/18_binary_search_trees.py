class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True


'''
SUGGESTED PROBLEMS

https://leetcode.com/problems/search-in-a-binary-search-tree/

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''