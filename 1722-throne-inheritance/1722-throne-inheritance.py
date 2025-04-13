class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = {}
        self.visited = set()
        self.start = kingName

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.graph:
            self.graph[parentName] = []
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.visited.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(node):
            if node not in self.visited:
                ans.append(node)

            for child in self.graph.get(node, []):
                dfs(child)
        dfs(self.start)
        return ans

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()