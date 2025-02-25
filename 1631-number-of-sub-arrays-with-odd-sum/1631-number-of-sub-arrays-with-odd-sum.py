class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        es=0
        sum1=0
        k=len(arr)
        for i in arr:
            sum1+=i
            if sum1%2==0:
                es+=1
        return ((k-es)*(es+1))%(pow(10,9)+7)

