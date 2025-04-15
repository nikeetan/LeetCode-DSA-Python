import heapq
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        #creating adjacency
        
        adj = defaultdict(list)
        for u, v, w in connections:
            adj[u].append((v , w))
            adj[v].append((u, w))

        visited = set()
        min_heap = []
        start_node = 1
        visited.add(start_node)
        
        # we added the possible neighbors from start node
        for neighbors in adj.get(start_node, []):
            nei, weigh = neighbors
            heapq.heappush(min_heap , (weigh, nei))

        
        # We have now have picked the node with the minimum weight
        total_weight = 0
        while min_heap and len(visited) < n:
            weight , node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_weight += weight

            for neighbor in adj.get(node, []):
                nei, wei = neighbor
                if neighbor not in visited:
                    heapq.heappush(min_heap, (wei , nei))
        
                
        return total_weight if len(visited) == n else -1



    


        return 0
            