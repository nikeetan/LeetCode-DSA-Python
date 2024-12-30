class Solution:
    def productExceptSelf(self,nums):
        res=[1]*len(nums)
        left_product,right_product=1,1
        l,r=0,len(nums)-1
        while l<len(nums) and r>=0:
            res[l]=res[l]*left_product
            res[r]=res[r]*right_product
            left_product=left_product*nums[l]
            right_product=right_product*nums[r]
            l+=1
            r-=1
        return res
            
