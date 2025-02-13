class Solution:
    def fib(self, n: int) -> int:
        if n>=2:
            dp=[[] for x in range(n+1)]
            dp[0]=0
            dp[1]=1
            for i in range(2,n+1):
                print(i,i-1,i-2)
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]
        else:
            if n==0:
                return 0
            else:
                return 1