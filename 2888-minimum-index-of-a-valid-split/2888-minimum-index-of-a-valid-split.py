class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        find dominant
        '''
        dominant_hash = {}
        for i in range(len(nums)):
            if nums[i] not in dominant_hash:
                dominant_hash[nums[i]] = 1
            else:
                dominant_hash[nums[i]] += 1
        dominant_ele = max(dominant_hash,key = dominant_hash.get)
        dominant_ele_count = 0
        for i in range(len(nums)):
            if nums[i] == dominant_ele:
                dominant_ele_count += 1
            if (dominant_ele_count) * 2 > (i + 1):
                if (dominant_hash[dominant_ele] - dominant_ele_count) * 2 > (len(nums) - (i + 1)):
                    return i
                else:
                    return -1
        return -1