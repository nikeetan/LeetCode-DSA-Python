class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        '''
        i will use bs to find the first positive index from there till
        '''
        pc,nc=0,0
        p1=0
        while p1<len(nums):
            if nums[p1]<0:
                nc+=1
            elif nums[p1]>0:
                pc+=1
            else:
                p1+=1
                continue
            p1+=1
        return max(nc,pc)
        