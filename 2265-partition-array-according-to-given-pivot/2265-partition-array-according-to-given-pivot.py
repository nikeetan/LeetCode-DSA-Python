class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        ans=[0]*n
        sl,l=0,len(nums)-1
        for i,j in zip(range(n),range(n-1,-1,-1)):
            if nums[i]<pivot:
                ans[sl]=nums[i]
                sl+=1
            if nums[j]>pivot:
                ans[l]=nums[j]
                l-=1
        while sl<=l:
            ans[sl]=pivot
            sl+=1
        return ans