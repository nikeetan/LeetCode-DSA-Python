'''
if digit sum is greater than target
carry = 1

9 9 5
    5
-----
100 0

Tc -> O(n)
Sc -> O(1)
'''

class Solution:
    def digitSum(self, num):
        total = 0 
        while num > 0:
            total += num % 10
            num = num // 10
        return total
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        if self.digitSum(n) == target:
            return 0
        else:
            carry = 0
            x = ''
            digit_sum = self.digitSum(n)
            while n > 0:
                digit = n % 10 + carry
                n = n // 10
                if digit_sum > target and digit > 0:
                    if len(x) != 0:
                        x = str(10 - digit) + x
                    else:
                        x = str(10 - digit)
                    carry = (digit + (10 - digit)) // 10
                    digit_sum = digit_sum - digit + carry           
                else:
                    if len(x) != 0:
                        x = '0' + x
                    else:
                        x = '0'
                    carry = 0
            return int(x)
                

        