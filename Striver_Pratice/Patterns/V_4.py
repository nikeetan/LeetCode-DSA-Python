'''
1
2 2 
3 3 3 
4 4 4 4
'''
class pattern:
    def __init__(self,size):
        self.size=size
    def printpattern(self):
        for i in range(self.size):
            for j in range(i+1):
                print(i+1,end=" ")
            print(" ")
n=int(input("Please enter the numbers of rows: "))
numbers=pattern(n)
numbers.printpattern()



        