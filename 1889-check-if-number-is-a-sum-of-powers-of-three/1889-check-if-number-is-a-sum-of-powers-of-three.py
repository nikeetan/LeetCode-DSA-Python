class Solution:
    '''
    Yedak or operation andre you will get true or f
    '''
    def helper(self,n,power):
        if n==0:
            return True
        if n<3**power:
            return False
        return self.helper(n-3**power,power+1) or self.helper(n,power+1)
    def checkPowersOfThree(self, n: int) -> bool:
        power=0
        return self.helper(n,power)

        
        