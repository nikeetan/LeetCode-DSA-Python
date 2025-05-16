# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def helper(root, parent):
            if root is None:
                return 0

            if not parent:
                rob = root.val + helper(root.left, parent = True) + helper(root.right, parent = True)
                not_rob = helper(root.left, parent = False) + helper(root.right, parent = False)
                return max(rob, not_rob)
            
            if parent:
                return helper(root.left, parent = False) +  helper(root.right, parent = False)
        
        return helper(root, parent = False)
