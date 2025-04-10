# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            stack = [root]
            sum_leaf = 0
            while stack:
                node = stack.pop()
                if node.left and (node.left.left is None) and (node.left.right is None):
                    sum_leaf += node.left.val
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return sum_leaf

