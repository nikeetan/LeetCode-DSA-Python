class Fibonacci:
    def Fibonacci_operation(self,no_of_terms):
        if no_of_terms==0:
            return 0
        if no_of_terms==1:
            return 1
        return self.Fibonacci_operation(no_of_terms-2)+self.Fibonacci_operation(no_of_terms-1)

no_of_terms=3
fibonacci=Fibonacci()
print(fibonacci.Fibonacci_operation(no_of_terms))