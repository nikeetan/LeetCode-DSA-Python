# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,root,p,q):
        if ((root is None) or (root==p) or (root==q)):
            return root
        l=self.helper(root.left,p,q)
        r=self.helper(root.right,p,q)
        if l and r:
            return root
        if not l:
            return r
        return l
        

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root,p,q)