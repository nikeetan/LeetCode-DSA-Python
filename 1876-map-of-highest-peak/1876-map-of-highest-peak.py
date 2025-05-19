class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        '''
        layer wise we should go
        '''
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # start point will be where i have water cell        
        R = len(isWater)
        C = len(isWater[0])
        queue = deque()
        for r in range(R):
            for c in range(C):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    isWater[r][c] = 0
                else:
                    isWater[r][c] = -1
        curr_height = 1
        while queue:
            layer = len(queue)
            for _ in range(layer):
                curr_x, curr_y = queue.popleft()
                
                for dirX, dirY in directions:
                    nei_x = curr_x + dirX
                    nei_y = curr_y + dirY
                    # checking inbounds
                    if ((0 <= nei_x < R) and (0 <= nei_y < C)) and isWater[nei_x][nei_y] == -1 :
                        isWater[nei_x][nei_y] = curr_height
                        queue.append((nei_x, nei_y))
            curr_height += 1
        return isWater


