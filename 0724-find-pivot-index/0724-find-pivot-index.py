class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                continue
            nums[i] = nums[i] + nums[i - 1]
        for i in range(len(nums)):
            if i == 0:
                if nums[-1] - nums[i] == 0:
                    return i
                continue
            if nums[i - 1] == nums[-1] - nums[i]:
                return i
        return -1
