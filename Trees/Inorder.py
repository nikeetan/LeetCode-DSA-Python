class Tree:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None
    
    def Insert_Element(self,data):
        if self.root<data:
            if self.right is None:
                self.right=Tree(data)
            else:
                self.right.Insert_Element(data)
        elif self.root>data:
            if self.left is None:
                self.left=Tree(data)
            else:
                self.left.Insert_Element(data)
    

    def Print_Inorder(self):
        if self.left:
            self.left.Print_Inorder()
        print(self.root)
        if self.right:
            self.right.Print_Inorder()
        


root=Tree(40)
root.Insert_Element(30)
root.Insert_Element(50)
root.Insert_Element(25)
root.Insert_Element(35)
root.Insert_Element(45)
root.Insert_Element(60)
root.Insert_Element(15)
root.Insert_Element(28)
root.Insert_Element(55)
root.Insert_Element(70)
root.Print_Inorder()


                