class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        i can solve it by two pointer
        '''
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1 & nums2)