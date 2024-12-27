# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        DFS
        inorder -> left -> root -> right
        '''
        enqueue=[]
        enqueue.append(root.left)
        enqueue.append(root.right)
        while enqueue:
            left=enqueue.pop(0)
            right=enqueue.pop(0)
            if ((left is None) and (right is None)):
                continue
            if ((left is None) or (right is None)):
                return False
            if left.val!=right.val:
                return False
            enqueue.append(left.left)
            enqueue.append(right.right)
            enqueue.append(left.right)
            enqueue.append(right.left)
        return True