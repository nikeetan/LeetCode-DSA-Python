# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,inorder_map,inorder,in_start,in_end,postorder,pos_start,pos_end):
        if in_start>in_end or pos_start>pos_end:
            return None
        root=TreeNode(postorder[pos_end])
        length=inorder_map[root.val]-in_start
        root.left=self.helper(inorder_map,inorder,in_start,inorder_map[root.val]-1,postorder,pos_start,pos_start+length-1)
        root.right=self.helper(inorder_map,inorder,inorder_map[root.val]+1,in_end,postorder,pos_start+length,pos_end-1)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}
        in_end=len(inorder)-1
        in_start=0
        pos_start=0
        pos_end=len(postorder)-1
        for i in range(len(inorder)):
            if inorder[i] not in inorder_map:
                inorder_map[inorder[i]]=i
        return self.helper(inorder_map,inorder,in_start,in_end,postorder,pos_start,pos_end)
        