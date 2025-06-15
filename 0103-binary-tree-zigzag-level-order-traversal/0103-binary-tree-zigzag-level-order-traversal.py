# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        BFS if the level is divisible by 2 reverse else the same
        i Know for every level 2 * i + 1 gives me the left child
        '''
        if root is None:
            return []
        queue = deque()
        start = root 
        queue.append(start)
        res = []
        level_cnt = 0
        while queue:
            lvl = len(queue)
            level_nodes = []
            for i in range(lvl):
                node = queue.popleft()
                if level_cnt % 2 != 0:
                    level_nodes.insert(0, node.val)
                else:
                    level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_nodes)
            level_cnt += 1
        return res

        