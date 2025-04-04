# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        process_queue = deque()
        process_queue.append(root.left)
        process_queue.append(root.right)
        while process_queue:
            left = process_queue.popleft()
            right = process_queue.popleft()
            if ((left is None) and (right is None)):
                continue 
            if ((left is None) or (right is None)):
                return False
            if left.val != right.val:
                return False
            process_queue.append(left.left)
            process_queue.append(right.right)
            process_queue.append(left.right)
            process_queue.append(right.left)
        return True