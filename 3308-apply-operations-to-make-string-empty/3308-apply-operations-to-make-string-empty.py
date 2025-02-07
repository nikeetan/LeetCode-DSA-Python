class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        d={}
        maxi=float('-inf')
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            maxi=max(maxi,d[i])
        d={}
        k=""
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]==maxi:
                k+=i
        return k
            
