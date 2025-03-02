class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1=0
        p2=0
        to_return=[]
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1][0]==nums2[p2][0]:
                to_return.append([nums1[p1][0],nums1[p1][1]+nums2[p2][1]])
                p1+=1
                p2+=1
            elif nums1[p1][0]<nums2[p2][0]:
                to_return.append(nums1[p1])
                p1+=1
            else:
                to_return.append(nums2[p2])
                p2+=1
        if p1==len(nums1):
            while p2<len(nums2):
                to_return.append(nums2[p2])
                p2+=1
        else:
            while p1<len(nums1):
                to_return.append(nums1[p1])
                p1+=1
        return to_return