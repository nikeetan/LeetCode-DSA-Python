'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *


[0,9,0]            lets say space printing range is from j in range (i)  how do you compute the star (2*(self.size-i)+1)
[1,7,1]
[2,5,2]
[3,3,3]
[4,1,4]
'''
class pattern:
    def __init__(self,size):
        self.size=size
    def printpattern(self):
        for i in range(self.size):
            for j in range(i):
                print(" ",end=" ")
            for j1 in range(2*(self.size-i)-1):
                print("*",end=" ")
            for j2 in range(i):
                print(" ",end=" ")
            print("")


n=int(input("Enter the number of rows :"))
stars=pattern(n)
stars.printpattern()