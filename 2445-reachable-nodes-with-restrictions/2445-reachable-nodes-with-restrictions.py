from collections import deque
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = defaultdict(list)
        start = 0
        seen = set()
        queue = deque()
        nodesVisited = 0

        #graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Setting the queue
        queue.append(start)
        seen.add(start)
        
        # Setting the restricted
        for node in restricted:
            seen.add(node)

        # Traverse the queue
        while queue:
            node = queue.popleft()
            nodesVisited += 1
            for nei in adj.get(node, []):
                if nei not in seen:
                    queue.append(nei)
                    seen.add(nei)
        return nodesVisited


        