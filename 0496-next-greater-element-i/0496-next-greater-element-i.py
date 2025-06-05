from  collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = defaultdict(list)
        stk = []
        n = len(nums2)
        for i in range(n - 1, -1 , -1):
            if stk:
                while stk and stk[-1] < nums2[i]:
                    stk.pop()
                if stk:
                    greater_map[nums2[i]] = stk[-1]
                else:
                    greater_map[nums2[i]] = -1
                stk.append(nums2[i])
            else:
                greater_map[nums2[i]]  = -1
                stk.append(nums2[i])
        res = []
        for i in nums1:
            res.append(greater_map[i])
        return res