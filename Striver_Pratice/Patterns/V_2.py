'''
*

* * 

* * *

* * * *
'''

class pattern:
    def __init__(self,size):
        self.size=size
    def printpattern(self):
        for i in range(self.size):
            for j in range(i+1):
                print("*",end=" ")
            print("")

n=int(input("Please enter the number of rows upto which pattern needs to be printed"))
star=pattern(n)
star.printpattern()



        