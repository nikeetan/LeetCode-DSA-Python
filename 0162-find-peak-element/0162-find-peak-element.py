class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2         
            if nums[mid] > nums[mid + 1]:
                r = mid
            elif nums [mid] < nums[mid + 1]:
                l = mid + 1
        return l

             
