class Solution:
    def __init__(self):
        pass
    def possible(self,bloomDay,day,k,m):
        no_of_bouquets=0
        j=0
        count=0
        while j<len(bloomDay):
            if bloomDay[j]<=day:
                count+=1
            else:
                no_of_bouquets+=(count)//k
                count=0
            j+=1
        no_of_bouquets+=(count)//k
        if no_of_bouquets>=m:
            return True
        return False
    def minDays(self,bloomDay,m,k):
        if len(bloomDay)<m*k:
            return -1
        else:
            left,right=min(bloomDay),max(bloomDay)
            while left<=right:
                mid=left+(right-left)//2
                if self.possible(bloomDay,mid,k,m):
                    right=mid-1
                else:
                    left=mid+1
            return left
fetch=Solution()
bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(fetch.minDays(bloomDay,m,k))