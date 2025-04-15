class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj.get(node, []):
                if (visited[neighbor] == True):
                    if parent != neighbor:
                        return True
                elif dfs(neighbor, node):
                    return True
            return False
 
        visited = [False] * n
        start = 0
        if dfs(start, -1):
            return False
        return all(visited)
