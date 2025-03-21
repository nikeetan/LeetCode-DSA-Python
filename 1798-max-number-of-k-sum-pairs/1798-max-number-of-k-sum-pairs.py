class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        p1,p2=0,len(nums)-1
        count=0
        while p1<p2:
            if nums[p1]+nums[p2]==k:
                count+=1
                p1+=1
                p2-=1
            elif nums[p1]+nums[p2]>k:
                p2-=1
            else:
                p1+=1
        return count

        