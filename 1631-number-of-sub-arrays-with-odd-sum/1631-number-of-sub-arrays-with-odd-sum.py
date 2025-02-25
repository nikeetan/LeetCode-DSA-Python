class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        os=0
        es=1
        sum1=0
        for i in range(len(arr)):
            sum1+=arr[i]
            if sum1%2==0:
                es+=1
            else:
                os+=1
        return (os*es)%(pow(10,9)+7)

