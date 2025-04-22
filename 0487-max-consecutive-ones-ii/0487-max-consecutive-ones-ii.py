'''
we can have a window where i have only one 0
[ 0 1 2 3 4 5 6 7 8 9 10 11 12 13
[ 0 0 0 0 0 0 1 1 1 1  0  1   1  1]
              l
                                 r
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) != 0:
            zero_count = 0
            left = 0
            maxi = float('-inf')
            for right in range(len(nums)):

                if nums[right] == 0:
                    zero_count += 1

                if zero_count > 1:
                    maxi = max(maxi, (right - left))
                    while left <= right and zero_count > 1:
                        if nums[left] == 0:
                            zero_count -= 1
                        left += 1
            if zero_count > 1:
                maxi = max(maxi, (right -  left))
            else:
                maxi = max(maxi , (right - left + 1))   
            return maxi
        else:
            return 0



