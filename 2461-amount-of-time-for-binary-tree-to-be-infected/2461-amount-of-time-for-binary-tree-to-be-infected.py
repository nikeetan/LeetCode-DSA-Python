# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.maxTime = 0
        def helper(root):
            if root is None:
                return -1, 0
            
            left_dist, left = helper(root.left)
            right_dist, right = helper(root.right)

            if root.val == start:
                self.maxTime = max(left, right)
                return 0, 1 + max(left, right)
            
            if right_dist != -1:
                self.maxTime = max(self.maxTime,  1 + right_dist + left)
                return 1 + right_dist , 1 + max(left, right)
            if left_dist != -1:
                self.maxTime = max(self.maxTime, 1 + left_dist + right)
                return 1 + left_dist, 1 + max(left , right)
            return -1, 1 + max(left, right)
        helper(root)
        return self.maxTime
