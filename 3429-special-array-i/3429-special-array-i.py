class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        p1=0
        p2=1
        while p2<len(nums):
            if ((nums[p1]%2==0 and nums[p2]%2!=0) or (nums[p1]%2!=0 and nums[p2]%2==0)):
                p1+=1
                p2+=1
                continue
            return False
        return True