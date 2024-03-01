class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def Insert_Element(self,data):
        try:
            if self.data:
                if self.data>data:
                    if self.left is None:
                        self.left=Node(data)
                    else:
                        self.left.Insert_Element(data)
                elif self.data<data:
                    if self.right is None:
                        self.right=Node(data)
                    else:
                        self.right.Insert_Element(data)
        except:
            print("Please Insert the valid Element")
    

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
        print(self.data)

root = Node(40)
root.Insert_Element(30)
root.Insert_Element(50)
root.Insert_Element(25)
root.Insert_Element(35)
root.Insert_Element(45)
root.Insert_Element(60)
root.Insert_Element(15)
root.Insert_Element(28)
root.Insert_Element(25)
print("Printing Tree Elements:")
root.PrintTree()

