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
        
        
        # queue for traversal
        queue = deque([source])                 # queue = [0]

        #visited set    
        visited = set()                         # []
                                                # destination = 2
        while queue:                            # queue = [0] , [1, 2] , [2, 2], [2]
            node = queue.popleft()              # node = 2 , queue = [2]
            # Adding the node is visited
            if node in visited:                 #2 in [0, 1, 2]
                continue
            else:
                visited.add(node)                   # [0, 1, 2]              
                if node == destination:             # 3 == 2
                    return True                     # True
                for neighbour in adj.get(node, []):   #[ 0 ]          
                    if neighbour not in visited:       # 0 in  [0, 1, 2]
                        queue.append(neighbour)        # queue = [ 2]
                    
        return False






        



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
                                                    