# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_bst(root, left_bound, right_bound):
            if (root is None):
                return True
            elif (root.val <= left_bound) or (root.val >= right_bound):
                return False
            return valid_bst(root.left, left_bound, root.val) and valid_bst(root.right, root.val,right_bound)
        return valid_bst(root, float('-inf'), float('inf')) 