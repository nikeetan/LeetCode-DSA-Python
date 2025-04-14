class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {}
        for u , v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):

            visited[node] = True

            for neighbors in adj.get(node, []):
                if not visited[neighbors]:
                    dfs(neighbors)

        visited = [False] * n
        connected_comp = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                connected_comp += 1
        return connected_comp
    




