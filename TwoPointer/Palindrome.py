import re
class Palindrome:
    def __init__(self,text):
        self.str=text
    def operation(self):
        new_string=''.join(re.findall("[a-zA-Z]",self.str))
        new_string=new_string.lower()
        left=0
        right=len(new_string)-1    
        while left<right:
            if new_string[left]!=new_string[right]:
                return "Non Palindrome"
            left+=1
            right-=1
        return "Palindrome"
text="A man, a plan, a canal: Panama"
instance=Palindrome(text)
print(instance.operation())
