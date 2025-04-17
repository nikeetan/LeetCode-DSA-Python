# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        def dfs(node):
            if node is None:
                return None
            path.append(str(node.val))
            left = dfs(node.left)
            right = dfs(node.right)
            if (left is None) and (right is None):
                res.append('->'.join(path))
            path.pop()
            return node.val
            
        dfs(root)
        print(res)
        return res
        '''
        during back tracking i should also remove the appended root val from path
        
        '''
        '''
        res=[[1, 2, 5], [1, 3]]
        '''