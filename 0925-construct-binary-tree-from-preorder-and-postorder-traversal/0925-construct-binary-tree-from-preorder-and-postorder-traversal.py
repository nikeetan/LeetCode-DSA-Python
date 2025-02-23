# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree(self,preorder,pre_start,pre_end,postorder,post_start,post_end,indx_map):
        if pre_start > pre_end or post_start > post_end:
            return None

       
        root = TreeNode(preorder[pre_start])

        if pre_start == pre_end:
            return root

       
        left_root_val = preorder[pre_start + 1]

       
        left_root_idx = indx_map[left_root_val]

        
        length = left_root_idx - post_start + 1

        
        root.left = self.tree(
            preorder, pre_start + 1, pre_start + length,  
            postorder, post_start, left_root_idx,         
            indx_map
        )

        # Recursively construct the right subtree
        root.right = self.tree(
            preorder, pre_start + length + 1, pre_end,    
            postorder, left_root_idx + 1, post_end - 1,   
            indx_map
        )

        return root

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indx_map={}
        for i in range(len(postorder)):
            indx_map[postorder[i]]=i
        return self.tree(preorder,0,len(preorder)-1,postorder,0,len(postorder)-1,indx_map)
        