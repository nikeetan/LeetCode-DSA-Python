class Solution:
    def scoreOfString(self, s: str) -> int:
        p2=1
        sum1=0
        while p2<len(s):
            sum1+=(abs(ord(s[p2-1])-ord(s[p2])))
            p2+=1
        return sum1
        

        