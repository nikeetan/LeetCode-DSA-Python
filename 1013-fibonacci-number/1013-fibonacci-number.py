class Solution:
    def memo(self,n,memory):
        if n in memory:
            return memory[n]
        if n<=1:
            return n
        memory[n]=self.memo(n-2,memory)+self.memo(n-1,memory)
        return memory[n]
    def fib(self, n: int) -> int:
        memory={}
        return self.memo(n,memory)



        
        