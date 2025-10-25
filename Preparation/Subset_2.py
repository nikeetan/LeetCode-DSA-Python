class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        result = []
        indx = 0
        def helper(indx, nums, sl):
            if indx == len(nums):
                result.append(sl[:])
                return 
            if indx > 0 and nums[indx] == nums[indx - 1]:
                return 
            sl.append(nums[indx])
            helper(indx + 1, nums, sl)
            sl.pop()
            helper(indx + 1, nums, sl)   
        helper(indx, nums, [])
        return result

find_subset = Solution()
nums = [1, 2, 2]
print(find_subset.subsetsWithDup(nums))
