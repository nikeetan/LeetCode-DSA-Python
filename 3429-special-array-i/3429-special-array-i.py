class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        else:
            p1,p2=0,1
            while p2<len(nums):
                if nums[p1]%2==0 and nums[p2]%2==0:
                    return False
                elif nums[p1]%2!=0 and nums[p2]%2!=0:
                    return False
                else:
                    p1+=1
                    p2+=1
            return True

        