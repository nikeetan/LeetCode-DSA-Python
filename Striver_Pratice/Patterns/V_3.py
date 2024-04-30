'''
1
1 2
1 2 3
1 2 3 4

'''
class pattern:
    def __init__(self,size):
        self.size=size
    def printpattern(self):
        for i in range(self.size):
            for j in range(i+1):
                print(j+1,end=" ")
            print("")

n=int(input("Enter the number of rows: "))
numbers=pattern(n)
numbers.printpattern()

        

    