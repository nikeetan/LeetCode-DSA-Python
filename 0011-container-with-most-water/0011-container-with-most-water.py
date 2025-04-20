class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        area = -1
        length = 0
        breadh = 0
        while p1 < p2:
            if height[p1] < height[p2]:
                length = height[p1]
                breadth = (p2 - p1)
                p1 += 1
            else:
                length = height[p2]
                breadth = (p2 - p1)
                p2 -= 1  
            area = max(area, length * breadth)
        return area


