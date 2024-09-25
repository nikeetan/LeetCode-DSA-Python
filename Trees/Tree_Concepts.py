class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
    def insertion(self,data):
        if self.val<data:
            if self.right==None:
                self.right=TreeNode(data)
            else:
                self.right.insertion(data)
        if self.val>data:
            if self.left==None:
                self.left=TreeNode(data)
            else:
                self.left.insertion(data)
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()



list1=[4,3,2,5,10]
root=TreeNode(90)
for i in list1:
    root.insertion(i)
root.inorder()