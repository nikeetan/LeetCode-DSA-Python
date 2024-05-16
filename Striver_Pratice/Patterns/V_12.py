'''
1     1
12    21
123  321
12344321
'''

class pattern:
    def __init__(self,row):
        self.row=row
    def printpattern(self):
        store=""
        #spaces=(self.row)*2
        for i in range(self.row):
            if store:
                store+=str(i+1)
            else:
                store=str(i+1)
            print(store,end="")
            for j in range(self.row-(i+1)):
                print("",end=" ")
            print(store[::-1],end="")
            print("")

p=pattern(int(input("Enter the row size upto which you need the numbers:")))
#p.test()
p.printpattern()        