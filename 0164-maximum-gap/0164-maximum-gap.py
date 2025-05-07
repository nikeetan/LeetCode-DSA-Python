class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        else:
            nums.sort()
            p1, p2 = 0, 1
            maxi = float('-inf')
            while p2 < len(nums):
                if nums[p2] - nums[p1] > maxi:
                    maxi = nums[p2] - nums[p1]
                p2 += 1
                p1 += 1
            return maxi
            