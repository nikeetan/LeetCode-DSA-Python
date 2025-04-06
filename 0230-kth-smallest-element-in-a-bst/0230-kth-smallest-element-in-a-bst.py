# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder (self, root):
        if root is None:
            return []
        else:
            left = self.inorder(root.left)
            right = self.inorder(root.right)
            return left + [root.val] + right
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_ele = self.inorder(root)
        return smallest_ele[k-1]