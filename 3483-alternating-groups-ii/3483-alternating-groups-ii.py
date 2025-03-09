class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors=colors+colors[0:k-1]
        count=0
        p1,p2=0,1
        while p2<len(colors): 
            if colors[p2]==colors[p2-1]:
                p1=p2
            if p2-p1+1==k:
                count+=1
                p1=p1+1
            p2+=1
        return count
