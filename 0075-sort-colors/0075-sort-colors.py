class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start,current,end=0,0,len(nums)-1
        while current<=end:
            if nums[current]==0:
                nums[start],nums[current]=nums[current],nums[start]
                start+=1
                current+=1
            elif nums[current]==1:
                current+=1
            elif nums[current]==2:
                nums[current],nums[end]=nums[end],nums[current]
                end-=1
        return nums
        # d={0:0,1:0,2:0}
        # for i in nums:
        #     d[i]+=1
        # for i in range(d[0]):
        #     nums[i]=0
        # for i in range(d[0],d[0]+d[1]):
        #     nums[i]=1
        # for i in range(d[0]+d[1],len(nums)):
        #     nums[i]=2