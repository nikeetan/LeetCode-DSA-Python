'''
i can think of this an n array tree
'''

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if col < 0 or col >= n:
                return float('inf') 
            if row == n - 1:
                return matrix[row][col]

            memo[(row, col)] = matrix[row][col] + min(
                dfs(row + 1, col),     
                dfs(row + 1, col - 1), 
                dfs(row + 1, col + 1)   
            )
            return memo[(row, col)]

        return min(dfs(0, col) for col in range(n))


            