class Solution:
    '''
    sort the second array in decreasing order
    and then when you pick the ele from nums1 we can traverse from nums2 and check which element is greater than the current element 
    o(n logn)
    all n2
    max heap and also i pop the elements use two variables
    prev , curr = -1, -1
    if curr == max pop 
    prev 
    monotonic stack

    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_max = {}
        stack = []
        p2 = len(nums2) - 1
        while p2 >= 0:                       # [1,3,4,2]                             
            while stack and stack[-1] < nums2[p2]: # [4, 3]       3 < 1
                stack.pop()                     
            if stack:                               # [4, 3]
                next_max[nums2[p2]] = stack[-1]     # {2 : -1 , 4 : -1, 3: 4, 1: 3}
            else:
                next_max[nums2[p2]] = -1           # {2 : -1 , 4 : -1 }
            stack.append(nums2[p2])             # [4, 3, 1]
            p2 -= 1
        print(next_max) # {2 : -1 , 4 : -1, 3: 4, 1: 3}
        # [4,1,2]
        #[-1, 3, -1]
        res = []
        for i in nums1:             # [4, 1, 2]
            res.append(next_max[i])     #res [-1 , 3, -1]
        return res

