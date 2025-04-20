class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp= [[0 for j in range(i)] for i in range(1, numRows+1)]
        dp[0][0] = 1
        for i in range(1, numRows):
            dp[i][0] = 1
            dp[i][-1] = 1
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp  

       