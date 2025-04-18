import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: 
        dist = [float('inf')] * n
        dist[src] = 0
        for i in range(k + 1):
            temp = dist.copy()
            for u, v, p in flights:
                if (dist[u]!= float('inf')) and (dist[u] + p < temp[v]):
                    temp[v] = dist[u] + p
            dist = temp
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
        #return -1 if float('inf') in dst else dist[dst]

