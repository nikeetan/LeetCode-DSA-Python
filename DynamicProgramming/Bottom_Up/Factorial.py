class Factorial:
    def __init__(self,number):
        self.dp_array=[1 if x==0 or x==1 else 0 for x in range(number+1)]
    def factotial_operation(self,number):
        for i in range(2,number+1):
            self.dp_array[i]=i * self.dp_array[i-1]
        return self.dp_array[number]

number=5
fact=Factorial(number)
print(fact.factotial_operation(number))