class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        ans=-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>0 and nums[mid-1]<=0:
                ans=mid
                break
            elif nums[mid]>0:
                right=mid
            else:
                left=mid+1
        if ans==-1 and nums[left]>0:
            ans=left
        left,right=0,len(nums)-1
        ans1=-1
        while left<right:
            mid=right+(left-right)//2
            if nums[mid]<0 and nums[mid+1]>=0:
                ans1=mid
                break
            elif nums[mid]<0:
                left=mid+1
            else:
                right=mid
        if ans1==-1 and nums[left]<0:
            ans1=left
        if (ans==-1) and (ans1==-1):
            return 0
        if ans1==-1:
            return len(nums)-ans
        elif ans==-1:
            return ans1+1
        else:
            return max(ans1+1,len(nums)-ans)
        