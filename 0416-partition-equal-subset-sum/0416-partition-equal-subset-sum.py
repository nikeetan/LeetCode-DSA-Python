class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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