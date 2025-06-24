import math
class Solution:
    def countTriples(self, n: int) -> int:
        # count = 0
        # for i in range(2, n):
        #     if (2 * i <= n) and (i ** 2 - 1) <= n and(i ** 2 + 1) <= n:
        #         count += 2
            
        # return count
        count = 0
        for p1 in range(1, n - 1):
            for p2 in range(p1 + 1, n):
                if math.sqrt(p1 ** 2 + p2 ** 2).is_integer() and math.sqrt(p1 ** 2 + p2 ** 2) <= n:
                    count += 2
        return count
                

