class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for (u , v, w) in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((w , v))
        
        
        # Min heap to determine i am standing at a node and what will be by next min
        min_heap = [(0, k)]

        #times
        min_times = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in min_times:
                continue
            
            min_times[node] = time
            for ntime, neighbour in adj.get(node, []):
                if neighbour not in min_times:
                    heapq.heappush(min_heap, ((time + ntime), neighbour))

        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1

                


    
        return 0 