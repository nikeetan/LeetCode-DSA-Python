class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        stack=[]
        ans=0
        for i in nums:
            while stack and stack[-1]>=i:
                ans=max(ans,sum(stack))
                stack=[]
            stack.append(i)
        if stack:
            ans=max(ans,sum(stack))
        return ans




        '''
        p1,p2,ascending,ans=0,1,nums[0],0
        while p2<len(nums):
            if nums[p2-1]<nums[p2]:
                ascending+=nums[p2]
            else:
                ans=max(ans,ascending)
                p1=p2
                ascending=nums[p1]
            p2+=1
        ans=max(ans,ascending)
        return ans
        '''