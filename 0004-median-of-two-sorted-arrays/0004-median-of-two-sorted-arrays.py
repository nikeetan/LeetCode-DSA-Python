class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        so if it was sort
        '''
        res = []
        p1, p2 = 0, 0
        def merge(nums1, nums2, p1, p2):
            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    res.append(nums1[p1])
                    p1 += 1
                else:
                    res.append(nums2[p2])
                    p2 += 1
          
            while p1 < len(nums1):
                res.append(nums1[p1])
                p1 += 1
            
            while p2 < len(nums2):
                res.append(nums2[p2])
                p2 += 1
        merge(nums1, nums2, p1, p2)
        if len(res)% 2 != 0:
            return res[len(res)//2]
       #print(res[len(res)//2] , res[(len(res)//2) - 1])
        return (res[(len(res)//2) - 1] + res[len(res)//2])/2
        