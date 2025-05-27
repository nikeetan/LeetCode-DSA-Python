class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def helper(indx):
            if indx in memo:
                return memo[indx]
            if indx >= n:
                return 0
            memo[indx] = nums[indx] + max(helper(indx + 2) , helper(indx + 3))
            return memo[indx]
        return max(helper(0), helper(1))
            