# class Dsu:
#     def __init__(self, n):
#         self.parent = [x for x in range(n)]
    
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def Union(self, x , y):
#         x = self.find(x)
#         y = self.find(y)

#         if x != y:
#             self.parent[x] = y
    
#     def isConnected(self, u, v):
#         return True if self.find(u) == self.find(v) else False 


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # BFS
        # adj list 
        adj = {}
        for u , v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)                    #{ 0 :[1, 2] , 1:[2], 2:[0]}
            adj[v].append(u)
        
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbour in adj.get(node, []):
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        return dfs(source)

        # Adjacency matrix
        # adj = {}
        # for n1, n2 in edges:
        #     if n1 not in adj:
        #         adj[n1] = []
        #     if n2 not in adj:
        #         adj[n2] = []
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)

        # visited = [False] * n
        # visited[source] = True
        # def dfs (curr_node):
        #     if curr_node == destination:
        #         return True                                     
        #     visited[curr_node] = True
        #     for neighbour in adj[curr_node]:
        #         if not visited[neighbour]:
        #             if dfs(neighbour):
        #                 return True        
        #     return False
        # return dfs(source)
                                                    