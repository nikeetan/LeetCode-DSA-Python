# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
inorder traversal of the BST gives the sorted order
'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        #complement_map = {}
        def dfs(root):
            if root is None:
                return []
            left = dfs(root.left)
            right = dfs(root.right)
            return left + [root.val] + right
        nums = dfs(root)
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            if nums[p1] + nums[p2] == k:
                return True
            elif nums[p1] + nums[p2] > k:
                p2 -= 1
            else:
                p1 += 1
        return False
        '''
        seen = set()
        def dfs(root):
            if root is None:
                return False
            if k - root.val in seen:
                return True
            seen.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)
        '''