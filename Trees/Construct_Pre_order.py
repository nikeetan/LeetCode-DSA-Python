class Node:
    def __init__(self,data):
        self.left = None
        self.right = None 
        self.data = data
class BinaryTree:
    def __init__(self):
        self.indx = -1 
    
    def buildTree(self,Nodes:list[int]):
        self.indx+=1
        if Nodes[self.indx] == -1:
            return None
        newNode = Node(Nodes[self.indx])
        newNode.left = self.buildTree(Nodes)
        newNode.right = self.buildTree(Nodes)

        return newNode

    def inordertraverse(self,root:Node):
        # left , root, right
        if root is None:
            return []
        left = self.inordertraverse(root.left)
        right = self.inordertraverse(root.right)
        return left + [root.data] + right
    
    def preordertraversal(self, root: Node):
        # root , left , right
        if root is None:
            return []
        data = root.data
        left = self.preordertraversal(root.left)
        right = self.preordertraversal(root.right)
        return [data] + left + right

    def postordertraversal(self, root: Node):
        #left , right , root
        if root is None:
            return []
        left = self.postordertraversal(root.left)
        right = self.postordertraversal(root.right)
        return left + right + [root.data]
        

pre_order = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
Tree = BinaryTree()

root = Tree.buildTree(pre_order)
print("The Root element of the tree is {}".format(root.data))

print("The Inorder Traversal is:",Tree.inordertraverse(root))

print("The Preorder Traversal is:",Tree.preordertraversal(root))


print(print("The Post order Traversal is:",Tree.postordertraversal(root)))