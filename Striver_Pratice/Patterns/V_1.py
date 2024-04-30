'''
*  *  *

*  *  *

*  *  *  

'''
class pattern:
    def __init__(self,size):
        self.size=size
    
    def print_pattern(self):
        for i in range(self.size):
            for j in range(self.size):
                print("*",end="")
            print("")
n=int(input("Please Enter the number of rows of matrix"))
star=pattern(n)
star.print_pattern()



