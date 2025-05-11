"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(root, res):
            if root is None:
                return root
            res.append(root.val)
            for child in root.children:
                dfs(child, res)
        dfs(root, res)
        return res
    '''
    iterative
    if root is None:
        return []
    stack = [root]
    output = []
    while stack:
        node = stack.pop()
        output.append(node.val)
        stack.extend(node.children[::-1])
    return output
    '''


