import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-x for x in gifts]
        heapq.heapify(gifts)
        count=0
        while count<k:
            x=heapq.heappop(gifts)
            heapq.heappush(gifts,-int(math.sqrt(-x)))
            count+=1
        return sum([-x for x in gifts]) 