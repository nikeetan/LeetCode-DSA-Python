'''
binary search on ans one pass on row and one pass on column 
left growth also and right growth also


row = [5, 5]
col = [3, 3]
'''

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        '''
        horizontal cuts
        '''
        row_sum = [0] * len(grid)
        col_sum = [0] * len(grid[0])

        for row in range(len(grid)):
            curr_sum = 0
            for col in range(len(grid[0])):
                curr_sum += grid[row][col]
            row_sum[row] = curr_sum

        for col in range(len(grid[0])):
            curr_sum = 0
            for row in range(len(grid)):
                curr_sum += grid[row][col]
            col_sum[col] = curr_sum

        prefix_row_sum = [0] * (len(grid) + 1)
        prefix_col_sum = [0] * (len(grid[0]) + 1)

        for i in range(len(row_sum)):
            prefix_row_sum[i + 1] = prefix_row_sum[i] + row_sum[i]
        total_sum = prefix_row_sum[-1]

        for i in range(1, len(grid)):
            if total_sum - prefix_row_sum[i] == prefix_row_sum[i]:
                return True
     
        for i in range(len(col_sum)):
            prefix_col_sum[i + 1] = prefix_col_sum[i] + col_sum[i]
        total_sum = prefix_col_sum[-1]

        for i in range(1, len(grid[0])):
            if total_sum - prefix_col_sum[i] == prefix_col_sum[i]:
                return True
        return False