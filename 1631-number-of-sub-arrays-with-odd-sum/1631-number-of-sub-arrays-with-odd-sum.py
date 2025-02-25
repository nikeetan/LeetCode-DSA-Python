class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        os=0
        es=1
        sum1=0
        count=0
        mod = 10**9 + 7
        for i in range(len(arr)):
            sum1+=arr[i]
            if sum1%2==0:
                count=(count+os)%mod
                es+=1
            else:
                count=(count+es)%mod
                os+=1
        return count

