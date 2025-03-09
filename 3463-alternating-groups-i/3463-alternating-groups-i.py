class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        p1=len(colors)-1
        p2=((p1+3)%len(colors))-1
        count=0
        while p2<len(colors):
            if ((colors[(p1+1)%len(colors)]!=colors[p1]) and (colors[(p1+1)%len(colors)] != colors[p2])):
                count+=1
            p1=(p1+1)%len(colors)
            p2+=1
        if ((colors[p1]!=colors[p1+1]) and (colors[p1+1]!=colors[p2%len(colors)])):
            count+=1
        return count


