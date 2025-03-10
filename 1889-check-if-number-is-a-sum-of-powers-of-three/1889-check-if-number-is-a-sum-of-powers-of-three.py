class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power=0
        while 3**power<=n:
            power+=1
        power-=1
        while n>0 and power>=0:
            if 3**power<=n:
                n=n-(3**power)
            if 3**power<n:
                return False
            power-=1
        return True if n==0 else False

        
        