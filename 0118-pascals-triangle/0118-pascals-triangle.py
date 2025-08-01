class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0 for j in range(i)] for i in range(1, numRows + 1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                if ((j == 0) or (j == len(dp[i]) - 1)):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp
            