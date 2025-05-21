class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, indx, sl):
            if indx == len(nums):
                res.append(sl)
                return 
            helper(nums, indx + 1, sl + [nums[indx]])
            helper(nums, indx + 1, sl) 
        helper(nums, 0 , [])
        return res