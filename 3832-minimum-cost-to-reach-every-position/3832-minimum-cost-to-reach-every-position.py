class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minCost = [0] * len(cost)
        left_min = float('inf')
        for i in range(len(minCost)):
            if cost[i] < left_min:
                left_min = cost[i]
            minCost[i] = left_min
        return minCost
        