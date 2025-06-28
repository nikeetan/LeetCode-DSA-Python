'''

brute force approach have a outer for loop and inner floop
while outer starts from 0 to n - 1 and inner starts from 1 till the end
maximum_sum = max(maximum_sum , nums[i] + nums[j])
when all the elements are same [1,1,1,1] k = 1
TC - > O(n ** 2)
SC - > O(n)

'''
import heapq
from collections import defaultdict
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        valtoindx = defaultdict(list)
        for indx, val in enumerate(nums):
            valtoindx[val].append(indx)
        nums.sort()
        cnt = 0 
        subseq = [0] * k
        max_heap = []
        
        for i in range(len(nums) - 1, -1 , -1):
            val_indx = valtoindx[nums[i]].pop()
            heapq.heappush(max_heap, (-1 * val_indx,nums[i]))
            cnt += 1
            if cnt == k:
                indx = k - 1
                while max_heap:
                    subseqindx, val = heapq.heappop(max_heap)
                    subseq[indx] = val
                    indx -= 1
                return subseq
        

            



