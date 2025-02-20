class Solution:
    def bin_insert(self,nums1,low,high,target):        
        while low<=high:
            mid=low+(high-low)//2
            if nums1[mid]==target:
                return mid+1
            elif nums1[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return low

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1)!=m:
            nums1.pop()
        for i in nums2:
            low=0
            high=len(nums1)-1
            nums1.insert(self.bin_insert(nums1,low,high,i),i)
        while len(nums1)>m+n:
            last=len(nums1)-1
            while last>=0 and nums1[last]!=0:
                last-=1
            nums1.pop(last)
        return nums1
        
            
