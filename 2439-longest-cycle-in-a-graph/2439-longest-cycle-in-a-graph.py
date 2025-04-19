class Solution:
    def __init__(self):
        self.ans = - 1


    def dfs (self, node, edges, visited, dist):
        visited [node] = True
        neighbor = edges[node]
        
        if neighbor != -1 and not(visited[neighbor]):
            dist[neighbor] = dist[node] + 1
            self.dfs(neighbor, edges, visited, dist)
        
        elif neighbor != -1 and neighbor in dist:
            self.ans = max(self.ans, (dist[node] - dist[neighbor] +1 ))

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        
        for i in range(n):
            if not visited[i]:
                dist = {i : 1}
                self.dfs(i, edges, visited, dist)
        return self.ans
        