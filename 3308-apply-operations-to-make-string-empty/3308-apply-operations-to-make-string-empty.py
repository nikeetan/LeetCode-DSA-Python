class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        if len(set(s))==len(s):
            return s
        else:
            d={}
            for i in range(len(s)):
                if s[i] not in d:
                    d[s[i]]=[i]
                else:
                    d[s[i]]+=[i]
            maxi=float('-inf')
            for key,values in d.items():
                maxi=max(len(values),maxi)
            to_return=[]
            for key,values in d.items():
                if len(values)==maxi:
                    to_return.append(values[-1])
            to_return=sorted(to_return)
            k=""
            for i in to_return:
                if len(k)==0:
                    k=s[i]
                else:
                    k+=s[i]
            return k