class Solution:
    def minChanges(self, s: str) -> int:
        p1,p2=0,1
        count=0
        while p2<len(s):
            if s[p1]!=s[p2]:
                count+=1
            p1+=2
            p2+=2
        return count


        