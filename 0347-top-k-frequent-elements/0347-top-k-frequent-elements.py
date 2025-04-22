import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ_map = Counter(nums)
        min_heap = []
        for key, values in occ_map.items():
            heapq.heappush(min_heap,(values, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [i[-1] for i in min_heap]
        
