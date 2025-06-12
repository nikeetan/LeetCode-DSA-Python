class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        p1 = 0
        diff = float('-inf')
        while p1 < len(nums):
            diff = max(diff, abs(nums[p1] - nums[(p1 + 1) % len(nums)]))
            p1 += 1
        return diff
