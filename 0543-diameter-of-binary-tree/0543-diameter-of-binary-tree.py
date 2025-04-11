# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        path = 0
        def dfs(root):
            nonlocal path
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            path = max(path, left + right)
            return 1 + max(left, right)
        dfs(root)
        return path