class Solution:
    # def helper(self,stack:list[int],bl:list[int],dict1,n:int,nums:List[int]):
    #     if n==len(nums):
    #         bl.append(stack[:])
    #         return
    #     for i in range(len(nums)):
    #         if dict1[nums[i]]!=1:
    #             dict1[nums[i]]=1
    #             stack.append(nums[i])
    #             self.helper(stack,bl,dict1,n+1,nums)
    #             stack.pop()
    #             dict1[nums[i]]=0
    def helper(self,bl:list[int],index:int,nums:list[int]):
        if index==len(nums):
            bl.append(nums[:])
            return
        for i in range(index,len(nums)):
            nums[i],nums[index]=nums[index],nums[i]
            self.helper(bl,index+1,nums)
            nums[i],nums[index]=nums[index],nums[i]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        # stack=[]
        # dict1={}
        # for i in nums:
        #     dict1[i]=0
        # bl=[]
        # n=0
        # self.helper(stack,bl,dict1,n,nums)
        # return bl
        bl=[]
        index=0
        self.helper(bl,index,nums)
        return bl
