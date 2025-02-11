class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        x=[sorted(x,reverse=True) for x in nums]
        sum1=0
        for j in range(len(x[0])):
            maxi=float('-inf')
            for i in range(len(x)):
                maxi=max(maxi,x[i][j])
            sum1+=maxi
        return sum1

