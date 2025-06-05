'''
from the first position i will maintain the monotinic increasing
if at all i reach the index where i have >= curr than i will just
include the stk size

similarly i can do for indx 1 
'''

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stk = []
        res = [0] * len(heights)
        n = len(heights)
        for i in range(n - 1, - 1, -1):
            pop_count = 0
            if stk:
                while stk and stk[-1] < heights[i]:
                    pop_count += 1
                    stk.pop()
                if pop_count == 0:
                    res[i] = 1
                elif pop_count > 0 and len(stk) == 0:
                    res[i] = pop_count
                else:
                    res[i] = pop_count + 1
                stk.append(heights[i])
            else:
                stk.append(heights[i])

        return res
