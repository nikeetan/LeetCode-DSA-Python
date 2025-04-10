# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        can i think of bfs here
        the root might be nOne rigth ?
        how big is the tree
        i am thinking of bfs like we will use a queue and check every time checking the node whether the child nodes  will be greater than the parent why i choose bfs because it says we are validating  BST and in BST we have exactly 2 child nodes for a parent node
        

        root = 5
        before appending we will check whether the root is > left and < right

        queue = []
        
        ele = 3 i dont have left as well as right for 3 

        '''
        

        def validate(root, low , high):
            if root is None:
                return True
            else:
                if (low != None and root.val <= low ) or (high != None and root.val >= high):
                    return False
                return validate(root.left, low, root.val)  and validate(root.right, root.val, high)
        return validate(root, None, None)
       

        