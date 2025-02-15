class Solution:
    def helper(self,s,d,indx):
        if indx==len(s):
            if d['A']>=2 or d['L']>=3:
                return False
            return True
        elif d['L']>=3:
            return False
        else:
            if s[indx]!='L':
                d['L']=0
            d[s[indx]]+=1
            return self.helper(s,d,indx+1)

    def checkRecord(self, s: str) -> bool:
        d={'A':0,'L':0,'P':0}
        indx=0
        return self.helper(s,d,indx)