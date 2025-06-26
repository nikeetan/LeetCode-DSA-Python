# k = 2
# 0.  1. 2  3.  4  5. 6  7. 8  9 10
# [1, 1, 1, 0 , 0, 0, 1, 1, 1, 1, 0]
#               st
#                                 en

# k = 3
# [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
#                                      st
#                                                        en
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_cnt = 0 
        start, end = 0, 0
        win_len = float('-inf')
        while end < len(nums):
            if nums[end] == 0:
                zero_cnt += 1
            if zero_cnt > k:
                win_len = max(win_len, end - start)
                while start < len(nums) and zero_cnt > k:
                    if nums[start] == 0:
                        zero_cnt -= 1
                    start += 1
            end += 1
        win_len = max(win_len, end - start)
        return win_len
        





        