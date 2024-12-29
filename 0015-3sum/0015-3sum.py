class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:                        
        nums=sorted(nums)
        curr=0
        target=0
        bl=set()
        while curr<len(nums)-2:
            low=curr+1
            high=len(nums)-1
            while low<high:
                triplet_sum = nums[low]+nums[curr]+nums[high]
                if triplet_sum == target:
                    bl.add((nums[curr],nums[low],nums[high]))
                    low+=1
                elif triplet_sum<target:
                    low+=1
                else:
                    high-=1
            curr+=1
        return [list(item) for item in bl]