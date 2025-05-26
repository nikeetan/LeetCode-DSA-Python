'''
i can apply topological but how it will be linear
'''

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = {}
        n = len(colors)
        dp = [[0]* 26 for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            if u not in adj:
                adj[u] = [v]
            else:
                adj[u].append(v)
            indegree[v] += 1
        
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1
        visited_count = 0
        max_count = 0
        while queue:
            
            node = queue.popleft()
            visited_count += 1
            max_count = max(max_count, max(dp[node]))
            for nei in adj.get(node, []):
                for i in range(26):
                    if i == ord(colors[nei]) - ord('a'):
                        dp[nei][i] = max(dp[nei][i] , dp[node][i] + 1)
                    else:
                        dp[nei][i] = max(dp[nei][i], dp[node][i])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
            
        if visited_count < n:
            return -1
        else:
            return max_count