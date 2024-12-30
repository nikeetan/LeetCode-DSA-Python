class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1=0
        p2=len(height)-1
        maxi=-1
        while p1<p2:
            if height[p1]>height[p2]:
                maxi=max(maxi,height[p2]*(p2-p1))
                p2-=1
            elif height[p1]<height[p2]:
                maxi=max(maxi,height[p1]*(p2-p1))
                p1+=1
            else:
                maxi=max(maxi,height[p1]*(p2-p1))
                p2-=1
        return maxi
