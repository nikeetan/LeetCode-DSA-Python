class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=[-1]*3
        p1=0
        cnt=0
        while p1<len(s):
            if s[p1]=='a':
                l[0]=p1
            if s[p1]=='b':
                l[1]=p1
            if s[p1]=='c':
                l[2]=p1
            cnt+=1+min(l)
            p1+=1
        return cnt
        # p1,p2=0,0
        # oc={'a':0,'b':0,'c':0}
        # cnt=0
        # while p2<len(s):
        #     oc[s[p2]]+=1
        #     while min(oc.values())==1:
        #         cnt+=len(s)-(p2)
        #         oc[s[p1]]-=1
        #         p1+=1
        #     p2+=1
        # return cnt