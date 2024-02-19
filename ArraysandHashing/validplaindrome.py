import re
def isPalindrome(s: str) -> bool:
    pattern="[a-zA-Z0-9]"
    s=s.lower()
    j=re.findall(pattern,s)
    p2=len(j)-1
    p1=0
    while p1<=p2:
        if j[p1]!=j[p2]:
            return False
        p1+=1
        p2-=1
    return True
    
s= "A man, a plan, a canal: Panama"
print(isPalindrome(s))