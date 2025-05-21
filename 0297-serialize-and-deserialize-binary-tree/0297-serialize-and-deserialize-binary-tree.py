# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []
        def preorder(node):
            if not node:
                res.append("M")
                return
            
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(res)  

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = data.split(',') 
        print(values)
        def helper():
            val = values.pop(0)  # pop from front
            if val == 'M':
                return None
            node = TreeNode(int(val))  
            node.left = helper()
            node.right = helper()
            return node

        return helper()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))