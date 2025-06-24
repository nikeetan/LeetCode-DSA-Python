'''
minimize the maximum stolen amount and ensuring atleast k houses are robbed
'''

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def is_possible(mid_amt):
            curr_house = 0 
            house_count = 0
            while curr_house < len(nums):
                if nums[curr_house] <= mid_amt:
                    house_count += 1
                    curr_house += 2
                    continue
                curr_house += 1
            return house_count >= k


        min_amt, max_amt = min(nums), max(nums)
        ans = min_amt
        while min_amt <= max_amt:
            mid_amt = min_amt + (max_amt - min_amt) // 2
            if is_possible(mid_amt):
                ans = mid_amt
                max_amt = mid_amt - 1
            else:
                min_amt = mid_amt + 1
        return ans
            