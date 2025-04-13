# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''

collecting the leaf nodes at that time if do a none

def fetchleaf(root)
[4, 5, 3]

def removeleaf
root.left and root.left and root.left.val in leafnode set
root.left = none
return

'''
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root):
            if root is None:
                return -1 
            left = dfs(root.left)
            right = dfs(root.right)
            height = 1 + max(left, right)
            if len(res) == height:
                res.append([])
            res[height].append(root.val)
            return height
        dfs(root)
        return res