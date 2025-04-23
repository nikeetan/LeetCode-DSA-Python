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
        if node is None:
            return node
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            
            curr_node = queue.popleft()

            for nei in curr_node.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    queue.append(nei)
                visited[curr_node].neighbors.append(visited[nei])
        return visited[node]

                



