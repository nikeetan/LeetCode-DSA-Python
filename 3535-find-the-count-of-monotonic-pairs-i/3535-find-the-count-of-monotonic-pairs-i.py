class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        
        max_limit = max(nums)
        mod = 10 ** 9 + 7 
        @cache
        def helper(indx, prev_a1, prev_a2):
            if indx >= len(nums):
                return 1
            pair_count = 0
            for curr_a1 in range(prev_a1, nums[indx] + 1):
                curr_a2 = nums[indx] - curr_a1
                if indx == 0 or curr_a2 <= prev_a2:
                    pair_count += helper(indx + 1, curr_a1, curr_a2)
            return pair_count
        return helper(0, 0, max_limit) % mod
        