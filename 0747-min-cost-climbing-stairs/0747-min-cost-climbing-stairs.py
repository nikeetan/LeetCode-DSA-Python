class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def helper(indx):
            if indx in memo:
                return memo[indx]
            if indx >= n:
                return 0
            memo[indx] = cost[indx] + min(helper(indx + 1), helper(indx + 2))
            return memo[indx]
        return min(helper(0),helper(1))