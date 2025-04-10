# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def validate(root, low , high):
        #     if root is None:
        #         return True
        #     else:
        #         if (low != None and root.val <= low ) or (high != None and root.val >= high):
        #             return False
        #         return validate(root.left, low, root.val)  and validate(root.right, root.val, high)
        # return validate(root, None, None)
        prev = float('-inf')
        def inorder(root):
            nonlocal prev 
            if root is None:
                return True
            if not inorder(root.left):
                return False
            if root.val <= prev:
                return False
            prev = root.val
            return inorder(root.right)
        return inorder(root)
    



        