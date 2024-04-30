'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''

class pattern:
    def __init__(self,size):
        self.size=size

    def printpatterns(self):
        for i in range(self.size):
            for j in range(self.size,i,-1):
                print(self.size-j+1,end=" ")
            print(" ")
n=int(input("Enter the number of rows: "))
Numbers=pattern(n)
Numbers.printpatterns()


        