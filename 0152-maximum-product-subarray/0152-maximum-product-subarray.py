'''
can i think of sliding window
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_seen = nums[0]
        min_seen = nums[0]
        for i in range(1, len(nums)):
            temp_max_seen, temp_min_seen = max_seen, min_seen
            max_seen = max(temp_max_seen * nums[i], temp_min_seen * nums[i], nums[i])
            min_seen = min(temp_min_seen * nums[i], nums[i], nums[i] * temp_max_seen)
            res = max(res, max_seen)
        return res