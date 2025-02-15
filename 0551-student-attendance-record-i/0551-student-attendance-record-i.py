class Solution:
    def checkRecord(self, s: str) -> bool:
        p1=0
        d={'A':0,'L':0,'P':0}
        while p1<len(s):
            if s[p1]!='L' and d['L']>0:
                d['L']=0
            d[s[p1]]+=1
            if d['A']>=2 or d['L']==3:
                return False
            p1+=1
        return True