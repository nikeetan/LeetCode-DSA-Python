import heapq
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        '''
        sort then in descending order and kind of subsequence like selecting not selecting with base condition being == k
        '''
        grid=[sorted(x,reverse=True) for x in grid]
        rows,cols=len(grid),len(grid[0])
        max_heap=[]
        sum1=0
        for i in range(rows):
            for j in range(min(limits[i],cols)):
                heappush(max_heap,-grid[i][j])
        for i in range(k):
            sum1+=-(heappop(max_heap))
        return sum1
                
        