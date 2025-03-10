class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        rem=0
        while n>1:
            rem=n%3
            n=n//3
            if rem!=0:
                return False
        return True if n==1 and rem==0 else False