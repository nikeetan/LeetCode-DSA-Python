# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
find maxof the list 

left = [0 : max]
right = [max :]

'''
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        find the maximum and get the index
        '''
        if not nums:
            return None
        else:   
            indx = -1
            ans = -1
            for i in range(len(nums)):
                if ans < nums[i]:
                    ans = nums[i]
                    indx = i
            
            root = TreeNode(ans)
            root.left = self.constructMaximumBinaryTree(nums[0 : indx])
            root.right = self.constructMaximumBinaryTree(nums[indx+1 : ])
            return root


        