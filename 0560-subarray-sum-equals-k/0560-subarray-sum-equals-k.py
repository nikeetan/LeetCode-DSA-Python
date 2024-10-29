class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        pre_hash = {0:1}
        count = 0
        for i in range(len(nums)):
            prefix_sum = prefix_sum + nums[i]
            if (prefix_sum - k) in pre_hash:
                count += pre_hash[prefix_sum-k]
            if prefix_sum not in pre_hash:
                pre_hash[prefix_sum]=1
            else:
                pre_hash[prefix_sum]+=1
        print(pre_hash)
        return count 



                