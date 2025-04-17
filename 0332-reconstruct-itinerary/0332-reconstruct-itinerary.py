import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Creating the adjancency list
        adj = defaultdict(list)
        for src , dst in sorted(tickets, reverse = True):
            adj[src].append(dst)
            
        start = 'JFK'
        res = []
      
        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            res.append(node)
        dfs(start)
        return res[::-1]
            