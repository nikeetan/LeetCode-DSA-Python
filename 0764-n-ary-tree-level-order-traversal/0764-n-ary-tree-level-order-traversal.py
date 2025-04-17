"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return root
        else:
            queue = deque([root])
            res = []
            while queue:
                gen = []
                level = len(queue)
                for i in range(level):
                    node = queue.popleft()
                    gen.append(node.val)
                    i = 0
                    while i < len(node.children):
                        queue.append(node.children[i])
                        i += 1
                res.append(gen)
            return res



            