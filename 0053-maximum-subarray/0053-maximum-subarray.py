class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float('-inf')
        sum1=0
        for i in nums:
            sum1+=i
            ans=max(ans,sum1)
            if sum1<0:
                sum1=0
        return ans