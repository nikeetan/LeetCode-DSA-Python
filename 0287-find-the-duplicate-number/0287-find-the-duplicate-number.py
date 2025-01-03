class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=sorted(nums)
        p1=0
        p2=1
        while p2!=len(nums):
            if nums[p1]==nums[p2]:
                return nums[p1]
            p1+=1
            p2+=1
        