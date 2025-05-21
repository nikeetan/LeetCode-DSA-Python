# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        good_nodes = 0
        stk = [(root, float('-inf'))]
        while stk:
            node, max_so_far = stk.pop()
            if max_so_far <= node.val:
                good_nodes += 1
            
            if node.left:
                stk.append((node.left, max(max_so_far, node.val))) 
            if node.right:
                stk.append((node.right, max(max_so_far, node.val))) 
        return good_nodes
        
            