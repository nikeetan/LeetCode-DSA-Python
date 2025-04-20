class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        pq = (max_diff, adjX, adjY)
        '''
        visited = [[False for j in range(len(heights[i]))] for i in range(len(heights))]
        diff_matrix = [[float('inf') for j in range(len(heights[i]))] for i in range(len(heights))]
        diff_matrix[0][0] = 0
        queue = [(0, 0, 0)]

        R = len(heights)
        C = len(heights[0])
        directions = [(-1,0),(1, 0),(0, -1),(0, 1)]
        while queue:
            diff,x, y = heapq.heappop(queue)
            # record in the visited
            visited[x][y] = True
        
            # fetch neighors
            for dir_x, dir_y in directions:
                adj_x = x + dir_x
                adj_y = y + dir_y
                if ((0 <= adj_x < R) and (0 <= adj_y < C)) and not(visited[adj_x][adj_y]):
                    curr_diff = abs (heights[x][y] - heights[adj_x][adj_y])

                    max_diff = max(curr_diff , diff_matrix[x][y])
                    if diff_matrix[adj_x][adj_y] > max_diff:
                        diff_matrix[adj_x][adj_y] = max_diff
                        heapq.heappush(queue, (max_diff, adj_x, adj_y))
        return diff_matrix[-1][-1]
            
            
