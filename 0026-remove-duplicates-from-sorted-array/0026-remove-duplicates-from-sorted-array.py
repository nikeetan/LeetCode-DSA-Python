class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        secondpointer = 1 
        unique_count = 0
        while secondpointer < len(nums):
            if nums[unique_count] != nums[secondpointer]:
                unique_count += 1
                nums[unique_count] = nums[secondpointer]
            secondpointer += 1
        return unique_count+1