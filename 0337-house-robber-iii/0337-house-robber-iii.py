# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def helper(root):
            if root is None:
                return 0, 0
                # rob, not rob
            left = helper(root.left)
            right = helper(root.right)

            rob = root.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return [rob, not_rob]
        return max(helper(root))