class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # kahns algorithm 
        indegree  = [0] * len(edges)
        for i in range(len(edges)):
            if edges[i] != -1:
                indegree[edges[i]] += 1

        # intializing the queue
        queue = deque()
        # adding the nodes whose indegree are 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        visited = [False] * len(edges)
        # reaching to the cycle
        while queue:
            node = queue.popleft()
            visited[node] = True
            nei = edges[node]
            if nei != -1:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        #lets check visited

        if all(visited):
            return -1
        else:
            # start with the first unvisited node
            ans = -1
            for i in range(len(edges)):
                nei = edges[i]
                if not(visited[i]):
                    cnt = 1
                    visited[i] = True
                    while nei != i:
                        visited[nei] = True
                        cnt += 1
                        nei = edges[nei]
                    ans = max(ans, cnt)
        return ans

    