#Om sai ram
class Fibonacci:
    def __init__(self,terms):
        self.dpArray=[0 if x==0 else 1 if x==1 else -1 for x in range(terms+1)]
    def fibonacci_operation(self,terms):
        if terms==0:
            return 0
        if terms==1:
            return 1
        if self.dpArray[terms]==-1:
            self.dpArray[terms]=self.fibonacci_operation(terms-1)+self.fibonacci_operation(terms-2)
        return self.dpArray[terms]

terms=20
Fibonacci_Series=Fibonacci(terms)
summ=Fibonacci_Series.fibonacci_operation(terms)
print(summ)