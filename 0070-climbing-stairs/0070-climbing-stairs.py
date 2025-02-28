class Solution:
    # def helper(self,steps,n,result,sl):
    #     if n<=0:
    #         if n==0:
    #             result.append(sl[:])
    #         return
    #     for i in steps:
    #         self.helper(steps,n-i,result,sl+[i])
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
    
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        steps = [1, 2]
        
        for i in range(2, n+1):
            for step in steps:
                if i - step >= 0:
                    dp[i] += dp[i-step]  # Add, don't min
                    print(dp)
        
        return dp[n]
        # dp=[float('inf') for i in range(n+1)]
        # dp[0]=0
        # coins=[1,2]
        # for i in range(1,len(dp)):
        #     for c in coins:
        #         if i-c>=0:
        #             dp[i]=min(dp[i],1+dp[i-c])
        # print(dp)
        # return dp[n]
