class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        # Create a adjacency list
        adj = defaultdict(list)

        for index, cost in enumerate(wells):
            adj[0].append((cost, index + 1))

        for conn in pipes:
            h1 , h2 , cost = conn
            adj[h1].append((cost, h2))
            adj[h2].append((cost, h1))

        
  
        # creating the visited node
        visited = set()
        min_heap = []
        start_well = 0
        for neighbors in adj.get(start_well, []):
            cost, node = neighbors
            heapq.heappush(min_heap,(cost, node))
        
        print(min_heap)

        # computing the traversal to visit the nodes
        total_cost = 0
        while min_heap and len(visited)< n+1 :
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_cost += cost
            

            for neighbors in adj.get(node, []):
                cost, nei = neighbors
                if nei not in visited:
                    heapq.heappush(min_heap,(cost, nei))
        return total_cost if len(visited) == n else -1

        