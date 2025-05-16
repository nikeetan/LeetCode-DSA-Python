class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            ans = float("-inf")
            # case 1 
            dp = [0] * (len(nums))
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
            for i in range(2, len(nums) - 1):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            ans = max(ans, dp[len(nums) - 2])

            # case 2
            dp = [0] * len(nums)
            dp[1] = nums[1]
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
            ans = max(ans, dp[len(nums) - 1])
            return ans

