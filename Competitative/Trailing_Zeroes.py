class Trailing_Zeroes:
    def __init__(self):
        self.zeros=0
        
    def fetch_zeroes(self,number):
        while number>=5:
            self.zeros+=number//5
            number=number//5
        return self.zeros
    
number=101
Number_of_Zeros=Trailing_Zeroes()
print(Number_of_Zeros.fetch_zeroes(number))

