class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pd={}
        to_return=[]
        for i in range(len(pattern)):
            if pattern[i] not in pd:
                pd[pattern[i]]=[i]
            else:
                pd[pattern[i]].append(i)
        cnt=0
        pd_ind={}
        for key,values in pd.items():
            pd_ind[cnt]=values
            cnt+=1     
        
        for i in words:
            wd={}
            for j in range(len(i)):
                if i[j] not in wd:
                    wd[i[j]]=[j]
                else:
                    wd[i[j]].append(j)
            cnt,flag=0,0
            for key,values in wd.items():
                if values!=pd_ind[cnt]:
                    flag=1
                    break
                cnt+=1
            if flag==0:
                to_return.append(i)
        return to_return

