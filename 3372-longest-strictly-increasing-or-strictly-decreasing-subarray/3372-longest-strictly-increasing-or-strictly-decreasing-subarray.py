class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        '''
        Strictly incresing
        '''
        p1,p2=0,1
        increasing=1
        decreasing=1
        while p2<len(nums):
            if nums[p2-1]<nums[p2]:
                print(nums[p1],nums[p2])
                increasing=max(increasing,p2-p1+1)
            else:
                p1=p2
            p2+=1
        print(increasing)
        p1,p2=0,1
        while p2<len(nums):
            if nums[p2-1]>nums[p2]:
                decreasing=max(decreasing,p2-p1+1)
            else:
                p1=p2
            p2+=1
        return max(increasing,decreasing)




