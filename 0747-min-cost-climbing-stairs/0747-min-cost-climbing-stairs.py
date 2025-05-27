class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        '''
        dp = [float('inf') for i in range(n + 1)]
        dp[n] = 0
        dp[n - 1] = cost[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])
        '''
        # TC : O(1)
        for i in range(n - 3 , -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
        
        