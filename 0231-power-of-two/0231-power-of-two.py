'''
1 0 0 0 
0 1 1 1 
0 
'''
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))

        