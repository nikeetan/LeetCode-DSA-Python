# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
inorder traversal of the BST gives the sorted order
'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        complement_map = {}
        def dfs(root):
            if root is None:
                return []
            left = dfs(root.left)
            right = dfs(root.right)
            return left + [root.val] + right
        nums = dfs(root)
        for i in nums:
            if k - i in complement_map:
                return True
            complement_map[i] = i
        return False
        