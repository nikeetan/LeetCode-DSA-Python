# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return []
            left = helper(root.left)
            right = helper(root.right)
            return left + [root.val] + right
        nums = helper(root)
        min_diff = float('inf')
        for i in range(len(nums) - 1):
            min_diff = min(min_diff, nums[i + 1] - nums[i])
        return min_diff