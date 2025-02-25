class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=0
        ps_map={0:1}
        count=0
        for i in nums:
            ps+=i
            if ps-k in ps_map:
                count+=ps_map[ps-k]
            if ps not in ps_map:
                ps_map[ps]=1
            else:
                ps_map[ps]+=1
        return count