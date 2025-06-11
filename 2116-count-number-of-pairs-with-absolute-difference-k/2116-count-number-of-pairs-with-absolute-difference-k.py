from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        valid_pairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    valid_pairs += 1
        return valid_pairs
                    