class Solution:
    def scoreOfString(self, s: str) -> int:
        p2=1
        l=[]
        while p2<len(s):
            l.append(abs(ord(s[p2-1])-ord(s[p2])))
            p2+=1
        return sum(l)
        

        