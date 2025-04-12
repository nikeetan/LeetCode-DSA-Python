# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # def is_leaf(node):
        #     if (node.left is None) and (node.right is None):
        #         return True
        
        # def find_leaf(root, res = []):
        #     if is_leaf(root):
        #         res.append(root.val)
            
        def dfs(root, res):
            if root is None:
                return 
            if (root.left is None) and (root.right is None):
                res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
        
        res1 = []
        res2 = []
        dfs(root1 , res1)
        dfs(root2 , res2)
        return res1 == res2

            
