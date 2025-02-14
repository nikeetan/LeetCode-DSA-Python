class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        p1=0
        maxi_1=float('-inf')
        maxi_0=float('-inf')
        start=0
        while p1<len(s):
            if s[p1]!='1':
                start=p1
                while p1<len(s) and s[p1]!='1':
                    p1+=1
                maxi_0=max(maxi_0,p1-start)
                start=p1
            maxi_1=max(maxi_1,p1-start+1)
            p1+=1
        return maxi_1>maxi_0

        