'''
        *
    *   *   *
 *   *  *  *   *
'''

class pattern:
    def __init__(self,size):
        self.size=size
    def printpattern(self):
        # Analyzed the number of columns
        '''
        [4,1,4]
        [3,3,3]
        '''
        for i in range(self.size):
            for j in range(self.size-i):
                print(" ",end=" ")
            for j1 in range(2*i+1):
                print("*",end=" ")
            for j in range(self.size-i):
                print(" ",end=" ")
            print("")

n=int(input("Enter the number of rows: "))
stars=pattern(n)
stars.printpattern()