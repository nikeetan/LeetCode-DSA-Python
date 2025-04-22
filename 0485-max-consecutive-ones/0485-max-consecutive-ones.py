class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = float('-inf')
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1      
            else:
                maxi = max(curr, maxi)
                curr = 0
        maxi = max(maxi, curr)
        return maxi
