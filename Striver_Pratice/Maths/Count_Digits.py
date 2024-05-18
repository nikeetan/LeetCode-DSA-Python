'''
Problem:
n=12345
count=5
'''
class count:
    def __init__(self,digit):
        self.number=digit 
    def operation(self):
        count=1
        while self.number//10!=0:
            count+=1
            self.number=self.number//10
        return count

Count_digits=count(int(input("Enter the number of which you want to find digits: ")))
print(Count_digits.operation())    