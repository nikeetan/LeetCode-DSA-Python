# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            to_visit=[root]
            final_list=[]
            while to_visit:
                maxi=float('-inf')
                level=len(to_visit)
                for i in range(level):
                    temp=to_visit.pop(0)
                    maxi=max(maxi,temp.val)
                    if temp.left:
                        to_visit.append(temp.left)
                    if temp.right:
                        to_visit.append(temp.right)
                final_list.append(maxi)
            return final_list