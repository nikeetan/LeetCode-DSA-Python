
'''
Basic logic is keep the counter from 2 as we know one divides any number till the number where we need the factors and examine and 
create a list which all satisfies the division logic 

Explored one logic where they traverse till square root of a number and find the numbers that are divisible
''' 
from Striver_Pratice.Maths.Check_Prime import prime
class factors:
    def __init__(self,k:int):
        self.number=k
    def operation(self):
        factors=2
        factors_list=[1]
        while factors<=self.number:
            if self.number%factors==0:
                factors_list.append(factors)
            factors+=1
        return factors_list
    def operation1(self):
        factors=2
        factors_list=[1]
        while factors<=int((self.number)**(1/2)):
            if self.number%factors==0:
                factors_list.append(factors)
                if self.number//factors not in factors_list:
                    factors_list.append(self.number//factors)
            factors+=1
        factors_list.append(self.number)
        factors_list.sort()
        return factors_list
    def operation2(self):
        k=self.operation1()
        new_list=[]
        for i in k:
            check_instance=prime(i)
            if check_instance.operation()=="Prime":
                new_list.append(i)
        return new_list

n=int(input("Please Enter the number of the factors do you want to fetch: "))    
find_fact=factors(n)
print("The factors of the number {} is {}".format(n,find_fact.operation()))
print("The factors of the number {} is {}".format(n,find_fact.operation1()))
print("The prime factors of the number {} are {}".format(n,find_fact.operation2()))

        