class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        mod = 10 ** 9 + 7
        max_hz = horizontalCuts[0]
        max_v = verticalCuts[0]

        for i in range(1, len(horizontalCuts)):
            max_hz = max(max_hz, horizontalCuts[i] - horizontalCuts[i - 1])
    
        for i in range(1, len(verticalCuts)):
            max_v = max(max_v, verticalCuts[i] - verticalCuts[i - 1])
        return (max_hz * max_v) % mod
        
            