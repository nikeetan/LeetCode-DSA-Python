'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
0 1 0 1 0 1
'''
class pattern:
    def __init__(self,size):
        self.size=size
    def patternprint(self):
        for i in range(self.size):
            if i%2==0:
                count=0
                for j in range(i+1):
                    if count==0:
                        count+=1
                        print(count,end=" ")
                    else:
                        count-=1
                        print(count,end=" ")
                print("")
            else:
                count=1
                for j in range(i+1):
                    if count==1:
                        count-=1
                        print(count,end=" ")
                    else:
                        count+=1
                        print(count,end=" ")
                print("")
n=int(input("Enter the number of rows: "))
numbers=pattern(n)
numbers.patternprint()

