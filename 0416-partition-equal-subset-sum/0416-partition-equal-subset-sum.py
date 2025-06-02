class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        memo = {}
        def dfs(indx, subset_sum):
            if (subset_sum, indx) in memo:
                return memo[(subset_sum, indx)]
            if subset_sum == 0:
                return True
            elif indx >= len(nums) or subset_sum < 0:
                return False
            memo[(subset_sum, indx)] = dfs(indx + 1, subset_sum - nums[indx]) or dfs(indx + 1, subset_sum)
            return memo[(subset_sum, indx)]


        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        return dfs(0, subset_sum)
        '''
        total = sum(nums)

        if total % 2 != 0:
            return False
        else:
            subset_sum = total // 2
            dp = [[False] * (subset_sum + 1) for _ in range(len(nums) + 1)]
            dp[0][0] = True
            for i in range(1, len(nums) + 1):
                dp[i][0] = True
                if i <= subset_sum:
                    dp[0][i] = False
            for i in range(1, len(nums) + 1):
                curr = nums[i - 1]
                for j in range(1, subset_sum + 1):
                    if j < curr:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
            return dp[len(nums)][subset_sum]