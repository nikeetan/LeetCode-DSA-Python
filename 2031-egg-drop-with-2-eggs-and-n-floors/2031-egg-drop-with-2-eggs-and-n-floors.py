class Solution:
    def twoEggDrop(self, n: int) -> int:
        moves = float('inf')
        memo = defaultdict(int)
        def helper(floor, egg):
            if (floor, egg) in memo:
                return memo[(floor, egg)]
            if floor == 0 or floor == 1:
                return floor
            if egg == 1:
                return floor
            res = float('inf')
            for i in range(1, floor):
                breaks = helper(i - 1, egg - 1)
                survives = helper(floor - i, egg)
                res = min(res, max(breaks, survives) + 1)
            memo[(floor, egg)] = res
            return res
        return helper(n, 2)




    