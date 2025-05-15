class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def helper(indx):
            if indx + 1 >= len(nums):
                return True
            for i in range(1, nums[indx] + 1):
                if helper(indx + i):
                    return True
            return False
        return helper(0)
