# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical (root, subroot):
            if (root is None) and (subroot is None):
                return True
            elif (root is None) or (subroot is None):
                return False
            elif root.val != subroot.val:
                return False
            return identical(root.left , subroot.left) and identical(root.right, subroot.right)
        
        def subtree(root, subroot):
            if root is None:
                return False
            if identical (root, subroot):
                return True
            return subtree(root.left, subroot) or subtree(root.right, subroot)
        
        return subtree(root, subRoot)

        