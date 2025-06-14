'''
9, 90, 10
tens place we can see 9 so basically we can group the number according to the first digit and sort among themselves which is bucket sort
'''

import heapq
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        class comparator(str):
            def __lt__(self, other):
                # a + b > b + a
                return self + other > other + self
        for  i, val in enumerate(nums):
            nums[i] = str(val)
        max_heap = []
        for i in nums:
            heapq.heappush(max_heap, comparator(i))
        while max_heap:
            res += heapq.heappop(max_heap)
        return "0" if len(res) == 0 or res[0] == '0' else res
        
            
