class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=[1 for i in range(len(nums))]
        left,right=0,len(nums)-1
        left_prod,right_prod=1,1
        while left<len(nums) and right>-1:
            x[left]=left_prod*x[left]
            left_prod=left_prod*nums[left]
            x[right]=right_prod*x[right]
            right_prod=right_prod*nums[right]
            left+=1
            right-=1
        return x