# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree(self,inorder,in_start,in_end,preorder,pre_start,pre_end,idx_map):
        if pre_start>pre_end or in_start>in_end:
            return None
        root=TreeNode(preorder[pre_start])
        length=idx_map[root.val]-in_start
        root.left=self.tree(inorder,in_start,in_start+length,preorder,pre_start+1,pre_start+length,idx_map)
        root.right=self.tree(inorder,idx_map[root.val]+1,in_end,preorder,pre_start+length+1,pre_end,idx_map)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map={}
        for i in range(len(inorder)):
            idx_map[inorder[i]]=i
        return self.tree(inorder,0,len(inorder)-1,preorder,0,len(preorder)-1,idx_map)