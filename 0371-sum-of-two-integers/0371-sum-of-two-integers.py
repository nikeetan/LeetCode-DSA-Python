class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        '''
        max_positive = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            temp = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = temp
        return a if a < max_positive else ~(a ^ mask)