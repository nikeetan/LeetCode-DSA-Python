class Solution:
    # def digit_sum(self,num1,num2):
    #     sum1=int(num1)+int(num2)
    #     return str(sum1%10)
    def hasSameDigits(self, s: str) -> bool:        
        while len(s)>2:
            p1=0
            new_number=''
            while p1<len(s)-1:
                new_number+=str((int(s[p1])+int(s[p1+1]))%10)
                p1+=1
            s=new_number
        return s[0]==s[1]
            
            
        