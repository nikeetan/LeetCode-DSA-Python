# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        total_len = 0
        path = []
        def dfs(root):
            nonlocal total_len, path
            if root is None:
                return 0 , []                                                                   
            left_height, left_path = dfs(root.left) # node 1 # node 2 # node 4 # 1 , [8] # 
            right_height, right_path = dfs(root.right) # node 9 

            if total_len < left_height + right_height : # 0 < 0
                total_len = left_height + right_height  
                path = left_path + [root.val] + right_path 

            if left_height >= right_height:         # 0 >= 0
                return 1 + left_height, left_path + [root.val]  # 1 , [8]
            else:
                return 1 + right_height, right_path + [root.val]
    
        dfs(root)
        return total_len
    '''
    path = [4, 2, 1, 3]
    or 
    [5, 2, 1, 3]
    '''



