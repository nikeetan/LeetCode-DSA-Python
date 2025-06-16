class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = float('-inf')
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_diff = max(max_diff, nums[j] - nums[i])
        return max_diff if max_diff != float('-inf') else -1