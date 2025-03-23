# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if root is None:
            return 0
        ## Lets find the parent of each node and also find the start where the disease spreading start from
        parent = {}
        queue = deque([root])
        start_node = None
        while queue:
            current_node = queue.popleft()
            if start == current_node.val:
                start_node = current_node
            if current_node.left:
                parent[current_node.left] = current_node
                queue.append(current_node.left)
            if current_node.right:
                parent[current_node.right] = current_node
                queue.append(current_node.right)
        if start_node is None:
            return 0
        
        # Now applying bfs
        visited = set()
        queue = deque([start_node])
        time =-1
        while queue:
            level = len(queue)
            time+=1
            for _ in range(level):
                current_node = queue.popleft()
                visited.add(current_node)
                if current_node in parent and parent[current_node] not in visited:
                    queue.append(parent[current_node])
                if current_node.left and current_node.left not in visited:
                    queue.append(current_node.left)
                if current_node.right and current_node.right not in visited:
                    queue.append(current_node.right)
        return time
