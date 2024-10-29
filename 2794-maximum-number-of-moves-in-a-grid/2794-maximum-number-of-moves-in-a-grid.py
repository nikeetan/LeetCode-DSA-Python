class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R , C = len(grid),len(grid[0])
        directions = [[0,1],[-1,1],[1,1]]
        @cache
        def dp(r,c):
            res = 0
            for x,y in directions:
                new_r = r+x
                new_c = c+y

                if 0<=new_r<R and new_c < C and grid[r][c]<grid[new_r][new_c]:
                    res = max(res, 1+dp(new_r,new_c))
            return res
        return max(dp(i,0) for i in range(R))
        