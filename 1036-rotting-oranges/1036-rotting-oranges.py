class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        create the queue which holds the starting point
        
        '''
        # Size of Row and Column
        R = len(grid)
        C = len(grid[0])
        # Create a visited
        visited = [[ 0 for _ in range(C)] for _ in range(R)]
        

        # Start nodes
        queue = deque()
        for row in range(R):
            for col in range(C):
               
                if grid [row][col] == 2:
                    queue.append((row, col , 0))
                    visited[row][col] = 2

                else:
                    visited[row][col] = 0
        




        # Traverse using Bfs and also like every time neighbours would be
        nei_row = [-1 , 0, +1, 0]
        nei_col = [0 ,  1,  0, -1]
        
        #Now Bfs
        timer = 0

        while queue:
            row, col , time = queue.popleft()
            timer = max(timer , time)

            for i in range(4):
                nrow = row + nei_row[i]
                ncol = col + nei_col[i]
    

                if ((nrow >= 0 and nrow < R) and (ncol >= 0 and ncol < C)):
                   
                    if ((visited[nrow][ncol] != 2) and (grid[nrow][ncol] == 1)):
                        queue.append((nrow, ncol, time + 1))
                
                        visited [nrow][ncol] = 2
        print(visited)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and visited [i][j] != 2:
                    return - 1
        return timer

            

        return timer

