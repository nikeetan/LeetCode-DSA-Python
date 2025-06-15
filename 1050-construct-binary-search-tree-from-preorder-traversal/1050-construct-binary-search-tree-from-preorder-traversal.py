# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        '''
        monotonic stack
        '''
        if len(preorder) == 0:
            return None
        else:
            stk = []
            root = TreeNode(preorder[0])
            curr_node = root
            stk.append(curr_node)
            for i in range(1, len(preorder)):
                curr_node = TreeNode(preorder[i])
                if curr_node.val < stk[-1].val:
                    stk[-1].left = curr_node
                else:
                    while stk and stk[-1].val < preorder[i]:
                        prev_node = stk.pop()
                    prev_node.right = curr_node
                stk.append(curr_node)
        return root