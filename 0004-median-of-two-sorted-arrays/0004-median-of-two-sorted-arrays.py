class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        symmetry
        '''
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)
        left = (n1 + n2 + 1) // 2

        # How many elements possible from first array
        l, r = 0, n1
        n = n1 + n2
        while l <= r:
            mid1 = (l + r) // 2
            mid2 = left - mid1

            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            print("info", left, (mid1, mid2))
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                #print(nums2, mid2)
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 0:
                    print(l1, l2, r1, r2)
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1
        return 0