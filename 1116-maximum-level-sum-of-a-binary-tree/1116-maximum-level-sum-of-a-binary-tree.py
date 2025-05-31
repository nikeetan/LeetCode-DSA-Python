# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        lvlsum = float('-inf')
        queue = deque()
        queue.append(root)
        level = 0
        curr_lvl = 0
        while queue:
            lvl = len(queue)
            curr_lvlsum = 0
            curr_lvl += 1
            for _ in range(lvl):
                node = queue.popleft()
                curr_lvlsum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if lvlsum < curr_lvlsum:
                lvlsum = curr_lvlsum
                level = curr_lvl
        return level

