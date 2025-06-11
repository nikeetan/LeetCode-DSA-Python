'''
recurssion
lets say player 1 chooses indx 0 or indx (n - 1)
what am i doing wrong in here adding index no i should be adding + 1 or - 1 for the index

'''

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        def helper(l, r):
            if l == r:
                return nums[l]
            return max(nums[l] - helper(l + 1, r), nums[r] - helper(l, r - 1))
        return helper(0, n) >= 0


            