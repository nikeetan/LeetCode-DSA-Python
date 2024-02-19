class Factorial:
    def __init__(self,number):
        self.dp_array=[1 if x==0 or x==1 else -1 for x in range(number+1)]

    def factorial_operation(self,number):
        if number==0 or number==1:
            return 1
        if self.dp_array[number]==-1:
            self.dp_array[number]=number * self.factorial_operation(number-1)
        return self.dp_array[number]
number=10            
fact=Factorial(number)
factorial=fact.factorial_operation(number)
print(factorial)