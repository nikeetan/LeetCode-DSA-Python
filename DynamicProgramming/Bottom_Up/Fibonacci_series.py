#Jai Sri Ram
class Bottom_Up_Fibonacci:
    def __init__(self,size):
        #initializing the matrix
        self.fib=[0 if x==0 else 1 if x==1 else 100 for x in range(size+1)]
        
    def fibonacci(self,no_of_terms):
        for i in range(2,no_of_terms+1):
            self.fib[i]=self.fib[i-1]+self.fib[i-2]
        return self.fib[no_of_terms]

term=5
dp_fibonacci=Bottom_Up_Fibonacci(term)
print(dp_fibonacci.fibonacci(term))

    