# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(node, curr_max):
            nonlocal good_nodes
            if node is None:
                return 0
            if curr_max <= node.val:
                good_nodes += 1
            dfs(node.left, max(node.val, curr_max))
            dfs(node.right, max(node.val, curr_max))
        dfs(root, float('-inf'))
        return good_nodes