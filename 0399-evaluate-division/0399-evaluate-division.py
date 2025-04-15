from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create adjanceny and wait list
        adj = defaultdict(list)

        for indx, edges in enumerate(equations):
            u, v  = edges
            adj [u].append([v, values[indx]])
            adj [v].append([u, 1/ values[indx]])

        # Bfs
        def bfs(source, destination):
            if (source not in adj) and (destination not in adj):
                return -1
            queue = deque([(source, 1)])
            visited = set()
            visited.add(source)
            while queue:
                node, wei = queue.popleft()
                if node == destination:
                    return wei
                for neighbor in adj.get(node, []):
                    nei, weight = neighbor
                    if nei not in visited:
                        queue.append((nei , wei * weight))
                        visited.add(nei)
            return -1
        res = []
        for i in queries:
            u, v = i
            res.append(bfs(u , v))

        # queries pass every queries record the result in a list
        return res