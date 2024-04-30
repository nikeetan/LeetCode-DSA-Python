'''

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

'''
class pattern:
    def __init__(self,size):
        self.size=size
    def printpattern(self):
        j=self.size
        for i in range(self.size):
            while j>=i+1:
                print(j,end=" ")
                j-=1
            print(" ")
            j=self.size
n=int(input("Please enter the number of rows : "))
Numbers=pattern(n)
Numbers.printpattern()