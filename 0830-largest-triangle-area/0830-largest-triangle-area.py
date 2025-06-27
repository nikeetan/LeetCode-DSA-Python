import math
class Solution:

    def calculateArea(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            return 0
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = float('-inf')
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    a = math.dist(points[i],points[j])
                    b = math.dist(points[j],points[k])
                    c = math.dist(points[k],points[i])
                    ans = max(ans, self.calculateArea(a, b, c))
        return ans

