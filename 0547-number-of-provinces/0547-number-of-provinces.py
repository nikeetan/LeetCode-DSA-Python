class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        
        def dfs(city):
            for neighbour in range(n):
                if ((isConnected[city][neighbour] == 1)and (visited[neighbour] == False)):
                    visited[neighbour] = True
                    dfs(neighbour)



        visited = [False] * n
        provinces = 0
        for city in range(n):
            if not visited[city]:
                dfs(city)
                visited[city] = True
                provinces += 1
        return provinces 