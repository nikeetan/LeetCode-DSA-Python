# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        left root right left root right
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
        '''

        def helper(left, right):
            # base condition
            if left > right:
                return None
            # choose the middle node as the root node
            if (left + right) % 2 != 0:
                mid = ((left + right) // 2 ) + 1
            else:
                mid = (left + right) // 2
            
        
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        left , right = 0 , len(nums) - 1
        return helper(left, right)
