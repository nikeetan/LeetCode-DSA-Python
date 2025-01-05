class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        nums=sorted(nums)
        p1=0
        p2=1
        while p2!=len(nums):
            if nums[p1]==nums[p2]:
                return nums[p1]
            p1+=1
            p2+=1
        '''
        '''
        hash_map={}
        for i in range(1,len(nums)+1):
            hash_map[i]=0
        for i in nums:
            if hash_map[i]!=0:
                return i
            else:
                hash_map[i]=1
        '''
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            if slow==fast:
                break
        return slow
        