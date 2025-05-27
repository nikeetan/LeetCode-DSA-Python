# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# bfs traversal the movement in which the left or right node is null we will just include the queue with some serialization with the letter to denote the null



'''
lvl = 0
# queue = [1]
lvl = 1 
# queue = [3, 2]
lvl = 2
# queue = [5, 3, -1, 9]
lvl = 3 
# queue = [-1, -1 , -1, -1]
TC : O(w)
SC : O(h) + o(2 ^ no of level s)
'''
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # queue [(start, level)]
        queue = deque([(root, 0)])
        ans = float('-inf')
        while queue:
            lvl = len(queue)
            start_indx = queue[0][1]
            for i in range(lvl):
                node, latest_indx = queue.popleft()
                if node.left:
                    queue.append((node.left, (2 * latest_indx + 1) - 1))
                if node.right:
                    queue.append((node.right, (2 * latest_indx + 2) - 1))
            
            ans = max(ans, (latest_indx - start_indx) + 1)
        return ans

