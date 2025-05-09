# A graph is a valid tree when we have no cycles in it how do we detect the cycle is dfs or bfs having the visit node and c

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
            for nei in adj.get(node, []):
                if visited[nei]:
                    if parent != nei:
                        return True
                elif dfs(nei, node):
                    return True
            return False

        visited = [False] * n
        start = 0
        if dfs(start, -1):
            return False
        return all(visited)
