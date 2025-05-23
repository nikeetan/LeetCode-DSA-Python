# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorder (self, root):
    #     if root is None:
    #         return []
    #     else:
    #         left = self.inorder(root.left)
    #         right = self.inorder(root.right)
    #         return left + [root.val] + right
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # smallest_ele = self.inorder(root)
        curr = root
        stack = []
        n = 0
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            if curr.right:
                curr = curr.right
            else:
                curr = None
            #return 1