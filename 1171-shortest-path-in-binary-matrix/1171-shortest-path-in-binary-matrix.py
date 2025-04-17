class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # fetch neighbor
                #   #   #
                #   #   #
               #    #   #
        directions = [(0, -1), (-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        #maximum row and col
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        def getdirections(cur_row , cur_col):
            for nxt_r , nxt_c in directions:
                new_r, new_c = cur_row + nxt_r, cur_col + nxt_c
                if not((0 <= new_r <= max_row) and (0 <= new_c <= max_col)):
                    continue
                if grid[new_r][new_c] != 0:
                    continue
                yield(new_r,  new_c)


        # checking whether the start and the end node are reachable
        if ((grid[0][0] != 0) or (grid[max_row][max_col] != 0)):
            return -1
        
        start = (0 , 0)
        queue = deque([start])
        grid[0][0] = 1

        dist = 0
      
        while queue:
            row , col = queue.popleft()
            dist = grid[row][col]

            if (row == max_row)  and (col == max_col):
                return dist
            
            for nei_r, nei_c in getdirections(row, col):
                grid[nei_r][nei_c] = dist + 1
                queue.append((nei_r, nei_c))
        return -1



