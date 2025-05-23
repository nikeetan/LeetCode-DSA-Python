class Solution:
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
                    dp[i] += dp[i-step]
        return dp[n]
       