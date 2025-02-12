import heapq
class Solution:
    def sum_digit(self,num):
        sum1=0
        while num!=0:
            sum1+=num%10
            num=num//10
        return sum1
    def maximumSum(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for i in nums:
            k=self.sum_digit(i)
            heappush(d[k],-i)
        maxi=float('-inf')
        for key,value in d.items():
            if len(value)>=2:
                maxi=max(maxi,(-1*heappop(d[key])+(-1*heappop(d[key]))))
        if maxi==float('-inf'):
            return -1
        else:
            return maxi
        
        
        