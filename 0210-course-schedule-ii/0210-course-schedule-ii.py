class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        course_order = []
        while queue:
            node = queue.popleft()
            course_order.append(node)
            for neighbour in adj.get(node,[]):
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return course_order if len(course_order) == numCourses else []