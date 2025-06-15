import math
class Solution:

    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        max_val = (1 << p) - 1  
        base = max_val - 1              
        exp = max_val // 2              
        return (pow(base, exp, mod) * max_val) % mod
