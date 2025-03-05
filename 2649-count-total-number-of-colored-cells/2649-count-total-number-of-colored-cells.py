class Solution:
    def coloredCells(self, n: int) -> int:
        dp=[0]*n
        dp[0]=1
        for i in range(1,n):
            dp[i]=4*(i)+dp[i-1]
        return dp[n-1]