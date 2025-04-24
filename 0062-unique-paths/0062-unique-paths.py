class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(m, n):
            if m == 1 or n == 1:
                return 1
            return dfs(m - 1, n) + dfs(m, n - 1)
        return dfs(m, n)