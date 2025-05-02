# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        count = 0
        res = ''
        def dfs(root):
            nonlocal count, res
            if root is None:
                return 
            dfs(root.left)
            for c in root.val:
                count += 1
                if count == k:
                    res = c
                    return 
            dfs(root.right)
        dfs(root)
        return res
    
                