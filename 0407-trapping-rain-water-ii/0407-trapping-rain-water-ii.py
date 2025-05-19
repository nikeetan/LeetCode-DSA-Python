import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # use min heap and include the values from the boundary
        min_heap = []
        R = len(heightMap)
        C = len(heightMap[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for r in range(R):
            for c in range(C):
                if (r == 0 or c == 0) or ((r == R - 1) or (c == C - 1)):
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        max_height = -1
        res = 0
        while min_heap:
            h, curr_r, curr_c = heappop(min_heap)
            max_height = max(max_height, h)
            res += max_height - h

            for dirx, diry in directions:
                nei_x, nei_y = curr_r + dirx, curr_c + diry
                if (nei_x < 0 or nei_x >= R) or (nei_y < 0 or nei_y >= C) or heightMap[nei_x][nei_y] == -1:
                    continue
                else:
                    heapq.heappush(min_heap, (heightMap[nei_x][nei_y], nei_x, nei_y))
                    heightMap[nei_x][nei_y] = -1
        return res



                            

        # use the formula max_height = max(max_height, h) rs += max_height - h
