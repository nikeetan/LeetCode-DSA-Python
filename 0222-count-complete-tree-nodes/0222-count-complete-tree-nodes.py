# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
i can think of bfs level order itself
'''
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root])
        node_count = 0
        while queue:
            level = len(queue)
            for _ in range(level):
                current_node = queue.popleft()
                node_count += 1
                if current_node.left or current_node.right:
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
        return node_count


        