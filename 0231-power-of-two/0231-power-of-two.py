'''
1 0 0 0 
0 1 1 1 
0 
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            rem = n % 2
            if rem != 0:
                return False
            n = n // 2
        return True if n > 0 else False

        