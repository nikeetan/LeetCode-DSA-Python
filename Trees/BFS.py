class Tree:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    def bfs(self,root)->list[int]:
        visited = [root]
        temp = root
        to_return = []
        while temp is not None:
            visited.append(temp.left)
            visited.append(temp.right)
            to_return.append(visited.pop(0).data)
            temp = visited[0]
        return to_return

root = Tree(10)
head = root
root.left = Tree(20)
root.right = Tree(30)
root.left.left = Tree(40)
root.left.right = Tree(50)
root.right.left = Tree(60)
root.right.right= Tree(70)

print(root.bfs(head))
