# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        que=[root]
        to_return=[]
        while que:
            temp=que.pop(0)
            if temp:
                if temp.val==val:
                    return temp
                if val<temp.val:
                    que.append(temp.left)
                else:
                    que.append(temp.right)
        return None
