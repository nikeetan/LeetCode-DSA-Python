# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        total_len = 0
        def dfs(root):
            nonlocal total_len
            if root is None:
                return 0
            left_height = dfs(root.left) #2 
            right_height = dfs(root.right) # 1 
            total_len = max(total_len, left_height + right_height)
            return 1 + max(left_height, right_height)
        dfs(root)
        return total_len
    



