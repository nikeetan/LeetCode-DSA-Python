# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        def is_leaf(node):
            return node is not None and (node.left is None and node.right is None)

        # Left Boundary
        def leftBoundary(node, res):
            curr = node.left
            while (curr):
                if not is_leaf(curr):
                    res.append(curr.val)                # 2
                if curr.left:                       
                    curr = curr.left
                else:
                    curr = curr.right
            print(res)
        # Leaf Nodes
        def leaf_nodes(node, res):
            if is_leaf(node):
                res.append(node.val)
                return
            if node.left:
                leaf_nodes(node.left, res)
            if node.right:
                leaf_nodes(node.right, res)
        # Right boundary
        def right_boundary(node, res):
            temp = []
            curr = node.right
            while(curr):
                if not(is_leaf(curr)):
                    temp.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            while temp:
                res.append(temp.pop())

        res = []
        if root is None:
            return res
        if not is_leaf(root):
            res.append (root.val)       # 1 
        
        leftBoundary(root, res)
        leaf_nodes(root, res)
        right_boundary(root, res)

        return res

            

        

        
        
