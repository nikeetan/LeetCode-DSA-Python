class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## Creating adjanceny and indegree
        adj = {}
        indegree = [0] * numCourses

        for next, prev in prerequisites:
            if prev not in adj:
                adj[prev] = [next]
            else:
                adj[prev].append(next)
            indegree[next] += 1
        
        # BFS queue

        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        # BFS
        node_visited = 0
        while queue:
            node = queue.popleft()
            node_visited += 1
            for neighbour in adj.get(node,[]):
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return node_visited == numCourses