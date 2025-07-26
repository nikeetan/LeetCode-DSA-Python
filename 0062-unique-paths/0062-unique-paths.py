class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if ((row == m - 1) and (col == n - 1)):
                return 1
            if (((row < 0) or (row >= m)) or ((col < 0) or (col >= n))):
                return 0
            memo[(row, col)] = helper(row + 1, col) + helper(row, col + 1)
            return memo[(row, col)]
        return helper(0, 0)