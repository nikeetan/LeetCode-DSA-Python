# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = float('-inf')
        def find_maximum ( root):                           # dfs(-10)
            nonlocal path_sum                               # left = 1
            if root is None:                                
                return 0                                    
            left = max(0,find_maximum(root.left))                  
            right = max(0, find_maximum(root.right))
            path_sum = max(path_sum , left + root.val + right)
            return root.val + max(left , right)
        find_maximum(root)
        return path_sum