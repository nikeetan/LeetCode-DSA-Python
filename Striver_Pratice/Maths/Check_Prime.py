'''
Traverse till the square root of a number and count the divisors if there are more than 1 divisor then you can say that the number is
not prime
'''
class prime:
    def __init__(self,n:int):
        self.number=n
    def operation(self):
        count=0
        i=1
        while i<=int((self.number)**(1/2)):
            if self.number%i==0:
                count+=1
                if self.number//i!=i:
                    count+=1
            if count>2:
                return "Non Prime" 
            i+=1
        return "Prime"
def __main__():
    n=int(input("Please Enter the number to check whether it is prime or not: "))
    k=prime(n)
    print("The following number {} is {}".format(n,k.operation()))


            