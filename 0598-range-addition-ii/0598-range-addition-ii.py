'''
what's the ops which has been occured more times that and doing m x n on that would be the 
best 
if all are equal then the minimum [a , b] would be my answer

4 cells -> 

all 9 cells  ->

all 9 cells ->

all 9 cells ->
 
4 cells -> 
'''

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        else:
            row, col = float('inf'), float('inf')
            for a , b  in ops:
                row = min(a, row)
                col = min(b, col)
            return row * col