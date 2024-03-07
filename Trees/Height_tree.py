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

    def Find_Height(self):
        if self.left:
            left=self.left.Find_Height()
        else:
            left=0
        if self.right:
            right=self.right.Find_Height()
        else:
            right=0
        return max(left,right)+1

T=Tree(1)
T.Insert_Element(0)
T.Insert_Element(3)
T.Insert_Element(4)
T.Insert_Element(5)
T.Insert_Element(6)
print(T.Find_Height())
#print(T.left.root)
#root.Print_Inorder()
#print(root.Find_Height())



    