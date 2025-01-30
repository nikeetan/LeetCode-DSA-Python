class Solution:
   
    def longestPalindrome(self, s: str) -> str:
        ind={}
        for i in range(len(s)):
            if s[i] not in ind:
                ind[s[i]]=[i]
            else:
                ind[s[i]].append(i)
        if len(ind)==1:
            return s
        else:
            to_return=""
            for i in range(len(s)):
                if len(ind[s[i]])==1:
                    continue
                else:
                    for j in ind[s[i]]:
                        p1=i
                        p2=-1
                        flag=0
                        if j!=p1:
                            p2=j
                        while s[p1]!=s[p2]:
                            p2-=1
                        if p1<p2:
                            cp1=p1
                            cp2=p2
                            while p1<p2:
                                if s[p1]!=s[p2]:
                                    flag=1
                                    break
                                else:
                                    p1+=1
                                    p2-=1
                            if ((flag==0) and (len(to_return)<cp2-cp1+1)):
                                to_return=s[cp1:cp2+1]
            if len(to_return)==0:
                return s[0]
            else:
                return to_return

                            
