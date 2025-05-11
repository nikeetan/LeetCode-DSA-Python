class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        m = len(nums2)
        sum1, zc1 = 0, 0
        sum2, zc2 = 0, 0
        for i in range(n):
            if nums1[i] == 0:
                sum1 += 1
                zc1 += 1
            sum1 += nums1[i]

        for j in range(m):
            if nums2[j] == 0:
                sum2 += 1
                zc2 += 1
            sum2 += nums2[j]

        if (zc1 == 0 and sum2 > sum1) or (zc2 == 0 and sum1 > sum2):
            return -1
        return max(sum1, sum2)
