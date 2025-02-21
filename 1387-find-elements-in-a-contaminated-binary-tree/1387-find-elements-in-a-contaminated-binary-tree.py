from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.d=defaultdict(int)
        self.dfs(root,0)

    def dfs(self,root,val):
        if root is None:
            return
        self.d[val]=1
        root.val=val
        self.dfs(root.left,2*val+1)
        self.dfs(root.right,2*val+2)

    def find(self, target: int) -> bool:
        return target in self.d
    
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)