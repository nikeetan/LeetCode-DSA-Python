class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        p1,p2,decreasing,ans=0,1,nums[0],0
        while p2<len(nums):
            if nums[p2-1]<nums[p2]:
                decreasing+=nums[p2]
            else:
                ans=max(ans,decreasing)
                p1=p2
                decreasing=nums[p1]
            p2+=1
        ans=max(ans,decreasing)
        return ans
        