class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum1=0
        while n!=0:
            digit=n%10
            prod*=digit
            sum1+=digit
            n=n//10
        return prod-sum1