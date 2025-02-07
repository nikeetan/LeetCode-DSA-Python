class Solution:
    def lastNonEmptyString(self, s: str) -> str:

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
        return "".join(s[i] for i in to_return)