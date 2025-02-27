class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[[0 for j in range(i+1)]for i in range(numRows)]
        for i in range(numRows):
            dp[i][0],dp[i][i]=1,1
            for j in range(1,len(dp[i])-1):
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        return dp