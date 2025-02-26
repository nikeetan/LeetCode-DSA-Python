class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ps=0
        min_ps=0
        ps=0
        for i in nums:
            ps+=i
            max_ps=max(max_ps,ps)
            min_ps=min(min_ps,ps)
        return abs(max_ps-min_ps)