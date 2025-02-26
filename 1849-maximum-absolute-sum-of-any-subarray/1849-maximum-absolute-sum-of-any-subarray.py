class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pf=float('-inf')
        min_pf=float('inf')
        sum1=0
        for i in nums:
            sum1+=i
            max_pf=max(max_pf,sum1)
            if sum1<0:
                sum1=0
        sum1=0
        for i in nums:
            sum1+=i
            min_pf=min(min_pf,sum1)
            if sum1>0:
                sum1=0
        return max(abs(max_pf),abs(min_pf))
