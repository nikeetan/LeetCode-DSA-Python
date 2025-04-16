class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # storing n
        n = len(graph)

        # start node
        start = 0
        destination = n - 1

        res = []
        path = [0]
      
        def dfs(node, path):
            if node == destination:
                res.append(path[:])
                return 
            else:
                for nei in (graph[node]):
                    path.append(nei)
                    dfs(nei, path)
                    path.pop()
        dfs(start, path)
        return res


            


