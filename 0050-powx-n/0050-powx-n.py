'''
2 * 2 * 2 * 2
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        power = n 
        if power < 0:
            power = -1 * n
        while power:
            if power % 2 == 1:
                ans = ans * x
                power = power - 1
            else:
                x = x * x
                power = power // 2
        if n < 0:
            ans = (1 / ans)
        return ans
