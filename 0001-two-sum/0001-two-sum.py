'''
p1, p2 = 0, len(nums) - 1
while p1 < p2: 
    current_sum = nums[p1] + nums[p2]
    if current_sum == target:
        return [p1, p2]
    elif current_sum > target:
        if nums[p1] > nums[p2]:
            p1 += 1
        else:
            p2 -= 1
    else:
        if nums[p1] < nums[p2]:
            p1 += 1
        else:
            p2 -= 1
return -1 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for idx in range(len(nums)):
            if ((target - nums[idx]) in hash_map) and idx != hash_map[(target - nums[idx])]:
                return [idx,hash_map[(target - nums[idx])]]
        return - 1
        