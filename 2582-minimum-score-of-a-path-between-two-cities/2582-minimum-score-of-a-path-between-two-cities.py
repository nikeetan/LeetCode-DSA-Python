'''
create an adjacency and can i solve it as a graph ?
'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Graph
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))

        queue = deque([(0, 1)])
        # weight, node
        ans = float('inf')
        visited = set()
        visited.add(1)
        while queue:
            curr_weight, curr_node = queue.popleft()
            
            for nei_info in adj.get(curr_node, []):
                nei_weight, nei_node  = nei_info
                ans = min(ans, nei_weight)
                if nei_node not in visited:
                    queue.append((nei_weight, nei_node))
                    visited.add(nei_node)
        return ans
        
        

        
        