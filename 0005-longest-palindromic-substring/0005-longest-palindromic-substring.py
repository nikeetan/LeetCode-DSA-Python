class Solution:
    def Expand(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
   
    def longestPalindrome(self, s: str) -> str:
        to_return=""
        for i in range(len(s)):
            n1=self.Expand(s,i,i)
            n2=self.Expand(s,i,i+1)
            if len(n1)>len(to_return):
                to_return=n1
            if len(n2)>len(to_return):
                to_return=n2
        return to_return





        '''
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
        '''

                            
