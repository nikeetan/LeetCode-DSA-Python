class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps_map={0:1}
        ps=0
        count=0
        for i in nums:
            ps+=i
            remainder=(ps%k)
            if remainder in ps_map:
                count+=ps_map[remainder]
                ps_map[remainder]+=1
            else:
                ps_map[remainder]=1
        return count 