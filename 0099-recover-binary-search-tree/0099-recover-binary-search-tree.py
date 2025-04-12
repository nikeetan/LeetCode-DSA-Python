# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        def swapped_nodes(nums):
            x, y = None , None
            for i in range(len(nums) - 1):
                if nums[i+1] < nums[i]:
                    y = nums[i+1]
                    if x is None:
                        x = nums[i]
                    else:
                        break
            return x, y
        def reconstruct(root, count):
            if root:
                if root.val == x or root.val == y:
                    root.val = y if x == root.val else x
                    count -= 1
                    if count == 0:
                        return 
                reconstruct(root.left, count)
                reconstruct(root.right, count)
        nums = inorder(root)
        x, y = swapped_nodes (nums)
        reconstruct(root, 2)