'''
        *
    *   *   * 
  *  *  *  *  *
  *  *  *  *  * 
    *   *   *
        *
'''


class pattern:
    def __init__(self,size):
        self.size=size
    def patternprint(self):
        '''
        
        [4, 1, 4]
        [3, 3, 3]
        [2, 5, 2]
        [1, 7, 1]
        [0, 9, 0]
        [0, 9, 0]
        [1, 7, 1]
        [2, 5, 2]
        [3, 3, 3]
        [4, 1, 4]

        '''
        #Forward Print
        for i in range(self.size):
            for j in range(self.size-i):
                print(" ",end=" ")
            for j1 in range(2*i+1):
                print("*",end=" ")
            for j2 in range(self.size-i):
                print(" ",end=" ")
            print("")
        #Reverse Print
        for i in range(self.size):
            for j in range(i+1):
                print(" ",end=" ")
            for j1 in range(2*(self.size-i)-1):
                print("*",end=" ")
            for j2 in range(i+1):
                print(" ",end=" ")
            print("")
n=int(input("Enter the number of rows: "))
Stars=pattern(n)
Stars.patternprint()