# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            queue = deque([root])
            visited = []
            while queue:
                level = len(queue)
                levelwise_nodes = []
                for current_level in range(level):
                    current_node = queue.popleft()
                    levelwise_nodes.append(current_node.val)
                    if current_node.left or current_node.right:
                        if current_node.left:
                            queue.append(current_node.left)
                        if current_node.right:
                            queue.append(current_node.right)
                visited.append(levelwise_nodes)
            if visited:
                p1,p2=0,len(visited)-1
                while p1<p2:
                    visited[p1],visited[p2] = visited[p2],visited[p1]
                    p1+=1
                    p2-=1
            return visited