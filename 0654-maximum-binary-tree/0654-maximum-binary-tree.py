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
        if i am the first maximum then we will insert to my left
        '''
        stack = []
        for num in nums:
            node = TreeNode(num)                #  5
            while stack and num > stack[-1].val :   # 0 -> 5
                node.left = stack.pop()
            
            if stack:                           #[6]
                stack[-1].right = node          #  3->2->1    6 -> 5 left 0
            stack.append(node)                  # [6, 0]
        return stack[0]
            
        