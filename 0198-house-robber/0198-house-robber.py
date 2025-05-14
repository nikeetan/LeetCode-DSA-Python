class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 2:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1] ,  max(nums[i], nums[i] + dp[i - 2]))
            print(dp)
            return dp[len(nums) - 1]
                
        return max(nums)