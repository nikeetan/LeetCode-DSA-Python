from collections import defaultdict
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        d=defaultdict(int)
        indx=0
        def helper(indx,d):
            if indx==len(rectangles):
                return d[max(d)]
            d[min(rectangles[indx])]+=1
            return helper(indx+1,d)
        return helper(indx,d)