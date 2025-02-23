# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree(self,inorder,in_start,in_end,postorder,post_start,post_end,indx_map):
        if post_start>post_end or in_start>in_end:
            return None
    
        root=TreeNode(postorder[post_end])
        length=indx_map[root.val]-in_start
        root.left=self.tree(inorder,in_start,indx_map[root.val]-1,postorder,post_start,post_start+length-1,indx_map)
        root.right=self.tree(inorder,indx_map[root.val]+1,in_end,postorder,post_start+length,post_end-1,indx_map)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indx_map={}
        for i in range(len(inorder)):
            indx_map[inorder[i]]=i
        return self.tree(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,indx_map)

        