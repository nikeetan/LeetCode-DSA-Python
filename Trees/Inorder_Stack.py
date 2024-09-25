class Tree:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

root=Tree(40)
root.left=Tree(30)
root.right=Tree(50)
print(root)

# stack=[]
# while True:
#     if root:
#         stack.append(root)
#         root=root.left
#     else:
#         if len(stack)==0:
#             break
#         root=stack.pop()
#         print(root.val)
#         root=root.right






