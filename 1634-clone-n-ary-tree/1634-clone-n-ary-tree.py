"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        else:
            cloned_tree = {}
            '''
            bfs
            '''
            queue = deque([root])
            while queue:
                lvl = len(queue)
                for _ in range(lvl):
                    node = queue.popleft()
                    if node not in cloned_tree:
                        cloned_tree[node] = Node(node.val, [])
                    for nei in node.children:
                        if nei not in cloned_tree:
                            cloned_tree[nei] = Node(nei.val, [])
                            queue.append(nei)
                        cloned_tree[node].children.append(cloned_tree[nei])
            return cloned_tree[root]

                

        