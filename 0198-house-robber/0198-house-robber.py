class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def helper(indx):
            if indx in memo:
                return memo[indx]
            if indx >= n:
                return 0
            memo[indx] = max(helper(indx + 1), nums[indx] + helper(indx + 2))
            return memo[indx]
        return helper(0)
            