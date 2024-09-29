class Solution:
    def scoreOfString(self, s: str) -> int:
        p1=0
        p2=1
        l=[]
        while p2<len(s):
            l.append(abs(ord(s[p1])-ord(s[p2])))
            p1+=1
            p2+=1
        return sum(l)
        

        