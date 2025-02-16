class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        p2=len(nums2)-1
        d=defaultdict(int)
        while p2>=0:
            if stack:
                while stack and stack[-1]<nums2[p2]:
                    stack.pop()
                if stack:
                    d[nums2[p2]]=stack[-1]
                else:
                    d[nums2[p2]]=-1
                stack.append(nums2[p2])
            else:
                d[nums2[p2]]=-1
                stack.append(nums2[p2])
            p2-=1
        to_return=[]
        for i in nums1:
            to_return.append(d[i])
        return to_return



