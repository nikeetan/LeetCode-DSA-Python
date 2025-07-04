# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        Paths = []
        def helper(root, pathsum, path):
            if root is None:
                return
            if(root.left is None) and (root.right is None):
                print("I am here")
                if pathsum - root.val == 0:
                    path.append(root.val)
                    Paths.append(path[:])
                    print (Paths)
            helper(root.left, pathsum - root.val, path + [root.val])
            helper(root.right, pathsum - root.val, path + [root.val])
        helper(root, targetSum, [])
        return Paths
