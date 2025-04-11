# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        bfs
        for eac level the nodes will be like 
        2 ** l 
        '''
        def bfs(root):
            if root is None:
                return []
            else:
                queue = deque([root])
                res = []
                while queue:
                    for level in range(len(queue)):
                        node = queue.popleft()
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                    res.append(node.val)
                return res
        return bfs(root)