import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # directions 
        directions = [(-1 , 0), (0, 1), (0, -1), (1, 0)]
        queue = []
        R, C = len(moveTime), len(moveTime[0])
        heapq.heappush(queue, (0, 0, 0))
        visited = set()
        while queue:
            curr_time , r, c = heapq.heappop(queue)
            
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if ((r == R - 1) and (c == C - 1)):
                return curr_time

            for dirx, diry in directions:
                nei_x, nei_y = r + dirx , c + diry
                if ((0 <= nei_x < R) and (0 <= nei_y < C)) and ((nei_x , nei_y) not in visited):
                    new_t = max(curr_time , moveTime[nei_x][nei_y]) + ((r + c) % 2 + 1)
                    heapq.heappush(queue, (new_t, nei_x, nei_y)) 
        
# TC : O(nm) becuase we will traverse the grid adding in the heap
       # adding and removal of the heap will generally be o(logn) here mn are the elements so o(logmn)
       # overall time complexity is o(mn)*log(mn)
# SC : O(mn) 
