class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Adjacency matrix
        adj = {}
        for n1, n2 in edges:
            if n1 not in adj:
                adj[n1] = []
            if n2 not in adj:
                adj[n2] = []
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = [False] * n
        visited[source] = True
        def dfs (curr_node):
            if curr_node == destination:
                return True                                     
            visited[curr_node] = True
            for neighbour in adj[curr_node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True        
            return False
        return dfs(source)
                                                    