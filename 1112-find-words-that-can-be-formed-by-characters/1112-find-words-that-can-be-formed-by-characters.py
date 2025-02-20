class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d1={}
        cnt=0
        for i in chars:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in words:
            flag=0
            d2={}
            for j in i:
                if j not in d2:
                    d2[j]=1
                    if j not in d1:
                        flag=1
                        break
                else:
                    d2[j]+=1
                    if ((j not in d1) or(d2[j]>d1[j])):
                        flag=1
                        break
            if flag==0:
                cnt+=len(i)
        return cnt
        