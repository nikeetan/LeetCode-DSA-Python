class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Adjacency matrix
        adj = {}
        for n1, n2 in edges:
            if n1 not in adj:
                adj[n1] = []
            if n2 not in adj:
                adj[n2] = []
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # Bfs queue holding the start node
        queue = deque([source])
        # Visted to track of visited nodes from the source
        visited = [False] * n
        visited[source] = True
        # Taversal
        # Approach is whenver in a visited i have my destination then the path exists
        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for neighbour in adj.get(node, []):
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

        return False




