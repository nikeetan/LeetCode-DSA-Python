# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_start(self, node, startValue):
        if node is None:
            return node
        if node.val == startValue:
            return node
        left = self.find_start(node.left, startValue)
        if left:
            return left
        return self.find_start(node.right, startValue )

    def parent_map(self, node, parent_map):
        '''
        dfs traversal intial node will have - 1 as parent or None
        '''
        if node is None:
            return
        if node.left:
            parent_map[node.left.val] = node
            self.parent_map(node.left, parent_map)
        if node.right:
            parent_map[node.right.val] = node
            self.parent_map(node.right, parent_map)

    def backtrack(self, node, path_tc):
        path = []
        while node in path_tc:
            path.append(path_tc[node][1])
            node = path_tc[node][0]
        path.reverse()
        return "".join(path)
    
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        '''
        convert tree to bidirectional graph
        parent table to facilitate node movement from node to its parent 
        first identify the starting node
        BFS to find shortest path                                       Direction
        path tracker record path taken to each node {node : parent, (Parent - > node)}
        Do still the start node when we reach the start node we can use a backtracking and also reversing the path
        '''
        # storing the parent_map
        parent_map = {}
        start_node = self.find_start(root, startValue)
        self.parent_map(root, parent_map)


        #bfs
        queue = deque([start_node])
        visited = set()
        visited.add(start_node)
        path_tc = {}

        while queue:
            curr_node = queue.popleft()
            if curr_node.val == destValue:
                return self.backtrack(curr_node, path_tc)

            # Fetch the parents
            if curr_node.val in parent_map:
                parent_node = parent_map[curr_node.val]
                if parent_node not in visited:
                    queue.append(parent_node)
                    visited.add(parent_node)
                    path_tc[parent_node] = (curr_node , "U")

            if curr_node.left and curr_node.left not in visited:
                queue.append(curr_node.left)
                path_tc[curr_node.left] = (curr_node , "L")
                visited.add(curr_node.left)

            if curr_node.right and curr_node.right not in visited:
                queue.append(curr_node.right)
                path_tc[curr_node.right] = (curr_node , "R")
                visited.add(curr_node.right)

        return " "



       