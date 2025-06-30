'''
i can think of this an n array tree
'''

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @lru_cache(None)
        def dfs(row, col):
            if col < 0 or col >= n:
                return float('inf') 
            if row == n - 1:
                return matrix[row][col]
            
            return matrix[row][col] + min(
                dfs(row + 1, col),     
                dfs(row + 1, col - 1), 
                dfs(row + 1, col + 1)   
            )

        return min(dfs(0, col) for col in range(n))


            