from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            queue = deque([root])
            depth = 0
            while queue:
                level = len(queue)
                depth += 1
                for current_level in range(level):
                    current_node = queue.popleft()
                    if current_node:
                        if current_node.left or current_node.right:
                            if current_node.left:
                                queue.append(current_node.left)
                            if current_node.right:
                                queue.append(current_node.right)
                        else:
                            return depth  
                    else:
                        return depth
            return depth

            