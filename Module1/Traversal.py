class Tree:
    def __init__(self,val):
        self.left=None 
        self.right=None
        self.val=val

def bfs(root):
    temp=root
    to_visit=[]
    to_visit.append(temp)
    bfs_l=[]
    while to_visit:
        if temp.left:
            to_visit.append(temp.left)
        if temp.right:
            to_visit.append(temp.right)
        value=to_visit.pop(0)
        bfs_l.append(value.val)
        if to_visit:
            temp=to_visit[0]
    return bfs_l



def inorder(root):
    '''
    DFS
    inorder -> left -> root -> right
    '''
    if root is None:
        return []
    else:
        left=inorder(root.left)
        right=inorder(root.right)
        return left+[root.val]+right

root=Tree(1)
temp=root
temp.left=Tree(2)
temp.right=Tree(3)
temp.left.left=Tree(4)
temp.left.right=Tree(5)
temp.right.left=Tree(6)
temp.right.right=Tree(7)

print(inorder(root))

print(bfs(root))
