# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if root is None:
                return 0
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            diameter = max(diameter , left_node + right_node)

            return 1 + max(left_node, right_node)
        dfs(root)
        return diameter

    '''
    path = [4, 2, 1, 3]
    or 
    [5, 2, 1, 3]
    '''



