'''
min_heap (dist, [3, 3]) every time we exceed k we will pop 
'''
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x1, y1 in points:
            dist = math.sqrt(x1**2 + y1**2)
            heapq.heappush(min_heap, (-dist, [x1, y1]))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = []
        while min_heap:
            dist, points = heapq.heappop(min_heap)
            res.insert(0, points)
        return res
            
