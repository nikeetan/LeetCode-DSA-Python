class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        p1,p2=0,0
        oc={'a':0,'b':0,'c':0}
        cnt=0
        while p2<len(s):
            oc[s[p2]]+=1
            while min(oc.values())==1:
                cnt+=len(s)-(p2+1)
                oc[s[p1]]-=1
                p1+=1
                cnt+=1
            p2+=1
        return cnt