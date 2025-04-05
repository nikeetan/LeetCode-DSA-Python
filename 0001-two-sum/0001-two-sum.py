
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if ((complement) in hash_map) and idx != hash_map[complement]:
                return [idx,hash_map[complement]]
        return - 1
        