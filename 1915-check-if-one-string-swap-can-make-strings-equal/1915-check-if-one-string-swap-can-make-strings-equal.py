class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if ''.join(sorted(list(s1)))==''.join(sorted(list(s2))):
            p1,p2=0,0
            unmatch=0
            while p1<len(s1):
                if s1[p1]!=s2[p2]:
                    unmatch+=1
                p1+=1
                p2+=1
            if unmatch==0 or unmatch==2:
                return True
        return False