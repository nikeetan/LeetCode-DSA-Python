class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Adjacency matrix
        adj = {}
        for u , v , w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((w , v))
        
        # Min heap for selection of minimum neighbour node
        min_heap = [(0, k)]

        # Record the node traversed and time taken
        visited = {}

        # Beigin the iterative traversal
        while min_heap:
            time_curr, curr_node = heapq.heappop(min_heap)

            if curr_node in visited:
                continue
            visited [curr_node] = time_curr

            for ntime, nnode in adj.get(curr_node, []):
                print(time_curr + ntime, nnode)
                if nnode not in visited:
                    heapq.heappush(min_heap, ((time_curr + ntime), nnode))
        if len(visited) == n:
            return max(visited.values())
        return -1

                    


