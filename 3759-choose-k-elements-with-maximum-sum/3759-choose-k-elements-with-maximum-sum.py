import heapq
class Solution:    
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        num_to_i = {}
        res  = [0] * len(nums1)
        for indx, val in enumerate(nums1):
            if val not in num_to_i:
                num_to_i[val] = [indx]
            else:
                num_to_i[val].append(indx)
        
        max_heap = []
        running_sum = 0
        for  val1, val2 in sorted(zip(nums1, nums2)):
            for i in num_to_i[val1]:
                res[i] = running_sum
            num_to_i[val1] = []
            running_sum += val2
            heapq.heappush(max_heap, (val2, val1))
            if len(max_heap) > k:
                value, _ = heapq.heappop(max_heap)
                running_sum -= value
        return res

