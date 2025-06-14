'''
9, 90, 10
tens place we can see 9 so basically we can group the number according to the first digit and sort among themselves which is bucket sort
'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        for i, val in enumerate(nums):
            nums[i] = str(val)
        
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))