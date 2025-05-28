class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        bfs
        '''
        R = len(mat)
        C = len(mat[0])
        # queue has row, col, steps
        queue = deque()
        steps = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        seen = set()
        for row in range(R):
            for col in range(C):
                if mat[row][col] == 0:
                    queue.append((steps, row, col))
                    seen.add((row, col))
        
        while queue:
            steps, curr_row, curr_col = queue.popleft()
            for offset_x, offset_y in directions:
                nei_x = curr_row + offset_x
                nei_y = curr_col + offset_y
                
                if ((0 <= nei_x < R) and (0 <= nei_y < C)) and ((nei_x, nei_y) not in seen):
                    mat[nei_x][nei_y] = steps + 1 
                    queue.append((steps + 1, nei_x, nei_y))
                    seen.add((nei_x, nei_y))
        return mat


                