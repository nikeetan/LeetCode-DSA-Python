import heapq
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        indegree = [0] * len(edges)
        max_score = float('-inf')
        node = None
        for u in range(len(edges)):
            v = edges[u]
            indegree[v] += u
        for v in range(len(indegree)):
            if indegree[v] > max_score:
                node = v
                max_score = indegree[v]
        return node

