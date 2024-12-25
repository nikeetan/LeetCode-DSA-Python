class Solution:
    def helper(self,bl:list[int],index:int,nums:list[int]):
        if index==len(nums):
            if nums[:] not in bl:
                bl.append(nums[:])
            return
        for i in range(index,len(nums)):
            nums[i],nums[index]=nums[index],nums[i]
            self.helper(bl,index+1,nums)
            nums[i],nums[index]=nums[index],nums[i]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        bl=[]
        index=0
        self.helper(bl,index,nums)
        return bl

        