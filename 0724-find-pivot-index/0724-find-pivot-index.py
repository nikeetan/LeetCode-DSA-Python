class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            total_sum = sum(nums)
            left = 0
            for curr in range(0, len(nums)):
                if total_sum - (left + nums[curr]) == left:
                    return curr
                left += nums[curr]
            return -1


