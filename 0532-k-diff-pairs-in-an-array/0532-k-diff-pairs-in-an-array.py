class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        hash_map = {}
        pairs_count = 0
        for indx in range(len(nums)):
            if(nums[indx] + k in nums[indx+1 :]) and((nums[indx] , nums[indx] + k) not in hash_map):
                hash_map[(nums[indx] , nums[indx] + k)] = 1
                pairs_count += 1
        print(hash_map)
        return pairs_count
