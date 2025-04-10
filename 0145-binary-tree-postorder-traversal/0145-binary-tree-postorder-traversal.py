# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        dsf
        '''
        def helper(root):
            if root is None:
                return []
            else:
                res = []
                stack = [root]
                while stack:
                    ele = stack.pop()
                    if ele.left:
                        stack.append(ele.left)
                    if ele.right:
                        stack.append(ele.right)
                    res.append(ele.val)
                return res [::-1]
        return(helper(root))

