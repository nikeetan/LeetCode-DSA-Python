class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(curr_row, curr_col):
            grid[curr_row][curr_col] = "0"
            for dirX, dirY in directions:
                nei_row = curr_row + dirX
                nei_col = curr_col + dirY
                
                if ((0 <= nei_row < R) and(0 <= nei_col < C) and (grid[nei_row][nei_col] != "0")):
                        dfs(nei_row, nei_col)
                        #mark visited
                       




        def bfs(curr_row, curr_col):
            grid[curr_row][curr_col] = '0'
            queue = deque([(curr_row, curr_col)])

    
            while queue:
                curr_row , curr_col = queue.popleft()
                for dirX, dirY in directions:
                    nei_row = curr_row + dirX
                    nei_col = curr_col + dirY
                    if ((0 <= nei_row < R) and(0 <= nei_col < C) and (grid[nei_row][nei_col] != "0")):
                        queue.append((nei_row, nei_col))
                        #mark visited
                        grid[nei_row][nei_col] = "0"
        
            

        # find the start point
        R, C = len(grid), len(grid[0])
        no_of_island = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    no_of_island += 1
                    #bfs(i, j)
                    dfs(i, j)
        return no_of_island

        
        
