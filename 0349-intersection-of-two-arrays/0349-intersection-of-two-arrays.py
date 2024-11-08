class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        i can solve it by two pointer
        '''
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1 & nums2)

        # res =[]
        # p1=0
        # while p1<len(nums1):
        #     p2=0
        #     while p2<len(nums2):
        #         if ((nums1[p1]==nums2[p2]) and(nums1[p1] not in res)):
        #             res.append(nums1[p1])
        #         p2+=1
        #     p1+=1
        # return res
        
