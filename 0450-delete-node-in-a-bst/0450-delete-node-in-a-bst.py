# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_successor(root):
            while root.left:
                root = root.left
            return root
        def find_predecessor(root):
            while root.right:
                root = root.right
            return root
            

        def dfs(root, key):
            if root is None:
                return root
            if key > root.val:
                root.right = dfs(root.right, key)
            elif key < root.val:
                root.left = dfs(root.left, key)
            else:
            # leaf Node
                if ((root.left is None) and (root.right is None)):
                    return None

                # if the node to be deleted has right then we will have to travel as much as left of the right sub tree to get the node and then swap so as to maintain the bst
                elif root.right:
                    successor = find_successor(root.right)
                    root.val = successor.val
                    root.right = dfs(root.right, successor.val)
                # if the node to be deleted has left then we will have to travel as much as right of the right sub tree to get the node and then swap so as to maintain the bst

                elif root.left:
                    predecessor = find_predecessor(root.left)
                    root.val = predecessor.val
                    root.left = dfs(root.left, predecessor.val)
            return root
        return dfs(root, key)
                    