# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def helper(root):
            if root is None:
                res.append("M")
                return
            
            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        res = data.split(",")        
        def helper():
            value = res.pop(0)
            if value == "M":
                return None
            root = TreeNode(int(value))
            root.left = helper()
            root.right = helper()
            return root
        return helper()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans