class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxi = 0
        current_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_streak = 1
                current_num = num
                while current_num + 1 in num_set:
                    current_streak += 1
                    current_num += 1
            maxi = max(maxi, current_streak)
        return maxi