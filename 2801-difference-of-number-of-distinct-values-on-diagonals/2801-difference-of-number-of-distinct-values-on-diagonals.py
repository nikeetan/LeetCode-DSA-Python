class Solution:
    def fetch_below(self,right,grid,row_ind,col_ind):
        while row_ind+1<len(grid) and col_ind+1<len(grid[0]):
            if grid[row_ind+1][col_ind+1] not in right:
                right[grid[row_ind+1][col_ind+1]]=1
            row_ind+=1
            col_ind+=1
        return len(right)
    def fetch_above(self,left,grid,row_ind,col_ind):
        while row_ind-1>=0 and col_ind-1>=0:
            if grid[row_ind-1][col_ind-1] not in left:
                left[grid[row_ind-1][col_ind-1]]=1
            row_ind-=1
            col_ind-=1
        return len(left)
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        rows,col=len(grid),len(grid[0])
        bl=[]
        for i in range(rows):
            sl=[]
            for j in range(col):
                left,right={},{}
                sl.append(abs(self.fetch_above(left,grid,i,j)-self.fetch_below(right,grid,i,j)))
            bl.append(sl)
        return bl


        
