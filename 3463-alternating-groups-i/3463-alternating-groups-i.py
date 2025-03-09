class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count=0
        for i in range(len(colors)):
            curr=colors[i]
            mid=colors[(i+1)%len(colors)]
            last=colors[((i+3)%len(colors))-1]
            if curr!=mid and mid!=last:
                count+=1
        return count