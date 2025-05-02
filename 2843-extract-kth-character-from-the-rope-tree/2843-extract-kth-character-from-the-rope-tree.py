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
        s = ""
        def dfs(root):
            if root is None:
                s = ""
                return s
            left = dfs(root.left)
            right = dfs(root.right)
            return left + root.val + right
        s = dfs(root)
        return s[k -1]
    
                