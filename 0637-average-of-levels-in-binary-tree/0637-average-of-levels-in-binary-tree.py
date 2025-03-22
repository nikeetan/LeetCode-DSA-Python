# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return
        else:
            queue = deque([root])
            visited = []
            while queue:
                level = len(queue)
                levelwise_nodes = 0
                for current_level in range(level):
                    current_node = queue.popleft()
                    levelwise_nodes += current_node.val
                    if current_node.left or current_node.right:
                        if current_node.left:
                            queue.append(current_node.left)
                        if current_node.right:
                            queue.append(current_node.right)
                visited.append(levelwise_nodes/level)
            return visited