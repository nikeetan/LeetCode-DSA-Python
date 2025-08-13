'''

3 2 1 0
0 0 1 1 = 9
0 0 1 0 = 8 
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            rem = n % 3
            if rem != 0:
                return False
            n = n // 3
        return True if n > 0 else False
