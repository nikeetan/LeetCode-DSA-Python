class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        i, j = 0, (len(nums) + 1)//2
        ans = len(nums)
        while ((i < len(nums)//2) and (j< len(nums))):
            if nums[i] < nums[j]:
                ans -= 2
            i += 1
            j += 1
        return ans
