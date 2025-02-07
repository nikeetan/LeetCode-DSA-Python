class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d={}
        color={}
        to_return=[]
        for i in queries:
            if i[0] in d:
                if color[d[i[0]]]-1==0:
                    del color[d[i[0]]]
                else:
                    color[d[i[0]]]-=1
            d[i[0]]=i[-1]
            if i[-1] not in color:
                color[i[-1]]=1
            else:
                color[i[-1]]+=1
            to_return.append(len(color))
        return to_return
