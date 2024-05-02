'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
class pattern:
    def __init__(self,size):
        self.size=size
    def printpattern(self):
        for i in range(self.size):
            for j in range(i+1):
                print("*",end=" ")
            print(" ")
        for i in range(self.size-1):
            for j in range((self.size-i)-1):
                print("*",end=" ")
            print(" ")

n=int(input("Enter the number of rows : "))
Stars=pattern(n)
Stars.printpattern()


        