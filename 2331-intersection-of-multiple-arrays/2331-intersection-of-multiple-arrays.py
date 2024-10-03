class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums)==1:
            return sorted(nums[0])
        else:
            list1=[]
            for i in range(len(nums)-1):
                list1=[x for x in nums[i] if x in nums[i+1]]
                nums[i+1]=list1
            return sorted(list1)
            