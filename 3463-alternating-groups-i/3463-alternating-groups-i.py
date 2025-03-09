class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count=0
        n=len(colors)
        for i in range(n):
            curr=colors[i]
            mid=colors[(i+1)%n]
            last=colors[((i+3)%n)-1]
            if curr!=mid and mid!=last:
                count+=1
        return count