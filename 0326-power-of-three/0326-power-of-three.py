class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power=0
        while 3**power!=n and 3**power<n:
            power+=1
        return 3**power==n
            