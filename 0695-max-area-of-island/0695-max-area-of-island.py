class Solution:
    def __init__(self):
        self.max = float('-inf')
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        def dfs(curr_row, curr_col):
            if ((curr_row < 0 or curr_row >= R) or (curr_col < 0 or curr_col >= C)) or grid[curr_row][curr_col] != 1:
                return 0
            grid[curr_row][curr_col] = 0 
            area = 1
            for dirX, dirY in directions:
                area += dfs(curr_row + dirX, curr_col + dirY)
            return area

        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    self.max = max(self.max, dfs(i, j))
        return self.max if self.max != float('-inf') else 0