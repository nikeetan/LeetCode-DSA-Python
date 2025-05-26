class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(indx):
            if indx in memo:
                return memo[indx]
            if indx == n:
                return 1
            if indx > n:
                return 0
            memo[indx] = helper(indx + 1) + helper(indx + 2)
            return memo[indx]
        return helper(0)