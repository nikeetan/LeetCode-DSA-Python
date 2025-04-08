class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hash_map ={}
        p1 = len(nums) - 1
        while p1 >= 0:
            if nums[p1] not in hash_map:
                hash_map[nums[p1]] = 1
            else:
                if (len(nums) - len(hash_map))%3 ==0:
                    return (len(nums) - len(hash_map)) // 3
                else:
                    return (len(nums) - len(hash_map)) // 3 + 1
            p1 -= 1
        return 0