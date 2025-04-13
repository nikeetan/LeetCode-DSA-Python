"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        head = node
        stk = [node]

        old_to_n = {node : Node(val = node.val)}

        while stk:
            node = stk.pop()
            for neighbour in node.neighbors:
                if neighbour not in old_to_n:
                    stk.append(neighbour)
                    old_to_n[neighbour] = Node(val = neighbour.val)
            
        for old in old_to_n:
            new = old_to_n[old]
            for neigbour in old.neighbors:
                new.neighbors.append(old_to_n[neigbour])

        return old_to_n[head]
