class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        os=0
        es=0
        sum1=0
        for i in arr:
            sum1+=i
            if sum1%2==0:
                es+=1
            else:
                os+=1
        return (os*(es+1))%(pow(10,9)+7)

