class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        elif len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        else:
            low,high=0,len(nums)-1
            while low<high:
                mid=low+(high-low)//2
                if ((nums[mid]>nums[mid-1]) and (nums[mid]>nums[mid+1])):
                    return mid
                elif nums[mid]<nums[mid+1]:
                    low=mid+1
                else:
                    high=mid
            return low
        

                    