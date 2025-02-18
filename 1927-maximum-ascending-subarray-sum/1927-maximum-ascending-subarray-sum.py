class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:     
            p1=0
            sum1=0
            maxi=float('-inf')
            while p1<len(nums)-1:
                if nums[p1]<nums[p1+1]:
                    sum1+=nums[p1]
                else:
                    sum1+=nums[p1]
                    maxi=max(maxi,sum1)
                    sum1=0
                    p1+=1
                    continue
                p1+=1
            
            if nums[p1]>nums[p1-1]:
                sum1+=nums[p1]
                maxi=max(maxi,sum1)
            return maxi
