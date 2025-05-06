class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [nums[nums[i]] for i in range(len(nums))]
        return res
        
        # TC : o(n)
        # SC : O(n)