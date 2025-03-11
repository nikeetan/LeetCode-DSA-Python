class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v={'a':0,'e':0,'i':0,'o':0,'u':0}
        ic=[]
        icc=0
        for i in range(len(word)):
            if word[i] not in v:
                ic.append(i)
        if ic:
            length=ic[icc]
        else:
            length=len(word)
        p1,p2,cnt=0,0,0
        while p2<len(word):
            if word[p2] in v:
                v[word[p2]]+=1
                while min(v.values())==1:
                    cnt+=length-p2
                    v[word[p1]]-=1
                    p1+=1
            else:
                icc+=1
                if icc<len(ic):
                    length=ic[icc]
                else:
                    length=len(word)
                p1=p2+1
                v={'a':0,'e':0,'i':0,'o':0,'u':0}
            p2+=1
        return cnt