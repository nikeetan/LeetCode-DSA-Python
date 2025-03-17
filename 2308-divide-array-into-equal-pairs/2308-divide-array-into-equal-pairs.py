class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map={}
        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        pairs=0
        for key,values in hash_map.items():
            if pairs>len(nums)//2:
                return False
            if values%2!=0:
                return False
            else:
                pairs+=values//2
        return True

