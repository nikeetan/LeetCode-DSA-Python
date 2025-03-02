class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in nums1:
            if i[0] not in d:
                d[i[0]]=i[1]
            else:
                d[i[0]]+=i[1]
        for i in nums2:
            if i[0] not in d:
                d[i[0]]=i[1]
            else:
                d[i[0]]+=i[1]
        key=sorted(d)
        to_return=[[i,d[i]] for i in key]
        return to_return


        