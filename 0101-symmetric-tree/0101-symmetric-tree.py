# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
i can do a level order traversal
queue = deque([root])
while queue:
    lvl = len(queue)
    for _ in range(lvl):
        node = queue.popleft()

'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root_left, root_right):
            if (root_left is None) and (root_right is None):
                return True
            if (root_left is None) or (root_right is None):
                return False
            return (root_left.val == root_right.val) and helper(root_left.right, root_right.left) and helper(root_left.left, root_right.right)
        return helper(root, root)
        