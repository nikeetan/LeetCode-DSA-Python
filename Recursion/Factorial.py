class Factorial:
    def factorial_operation(self,n):
        if n==0:
            return 1
        if n==1:
            return 1
        else:
            return n * self.factorial_operation(n-1)
fact=Factorial()
print(fact.factorial_operation(5))