'''
if i reach the destination with the positive health then i should return true
TC -> O(M X N)
SC -> O(M X N)
'''
from collections import deque
import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        #initialization
        queue = []
        if grid[0][0] == 0:
            # decrease_health, row, col
            start = (0, 0, 0)
        else:
            start = (1, 0, 0)
        R = len(grid)
        C = len(grid[0])
        seen = set()
        heapq.heappush(queue, start)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        seen.add((0, 0))
        # Traverse
        while queue:
            decrease, row , col = heapq.heappop(queue)
            if health - decrease <= 0:
                return False
            if (health - decrease >= 1) and row == R - 1 and col == C - 1:
                return True
            for dirX, dirY in directions:
                offsetX = row + dirX
                offsetY = col + dirY
                if ((0 <= offsetX <= R - 1) and (0 <= offsetY <= C - 1) and (offsetX, offsetY) not in seen):
                    if grid[offsetX][offsetY] == 1:
                        heapq.heappush(queue, (decrease + 1, offsetX, offsetY))
                    else:
                        heapq.heappush(queue, (decrease, offsetX, offsetY))
                    seen.add((offsetX, offsetY))
                    
        return False