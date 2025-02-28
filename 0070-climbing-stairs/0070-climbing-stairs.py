class Solution:
    # def helper(self,steps,n,result,sl):
    #     if n<=0:
    #         if n==0:
    #             result.append(sl[:])
    #         return
    #     for i in steps:
    #         self.helper(steps,n-i,result,sl+[i])
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]