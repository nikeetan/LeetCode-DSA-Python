class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        grow right and then come left
        '''
        low,high=0,len(nums)-1
        while low<=high:
            if nums[low]<=nums[high]:
                return nums[0]
            else:
                mid=low+(high-low)//2
                if nums[mid+1]<nums[mid]:
                    return nums[mid+1]
                elif nums[mid-1]>nums[mid]:
                    return nums[mid]
                elif nums[mid]>nums[low]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
