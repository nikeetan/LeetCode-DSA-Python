import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # classic Dijiktras
        visited = set()
        # Row and column 
        R = len(moveTime)
        C = len(moveTime[0])
        # maintianing the queue as  (t, r, c)
        start = (0, 0 , 0)
        queue = []
        heapq.heappush(queue, start)   
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            curr_t, r, c = heapq.heappop(queue)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if ((r == R - 1) and (c == C - 1)):
                return curr_t
            for dirX, dirY in directions:
                nei_x , nei_y = r + dirX, c + dirY
                if ((0 <= nei_x < R and 0<= nei_y < C) and (nei_x, nei_y) not in visited):
                    new_t = max(curr_t, moveTime[nei_x][nei_y]) + 1 
                    heapq.heappush(queue, (new_t, nei_x, nei_y))
        return - 1
        

        