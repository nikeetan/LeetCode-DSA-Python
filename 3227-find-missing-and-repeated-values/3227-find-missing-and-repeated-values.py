class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        to_return=[]
        rows,cols=len(grid),len(grid[0])
        arr=[False]*(rows*rows)
        for i in range(rows):
            for j in range(cols):
                if arr[grid[i][j]-1]:
                    to_return.append(grid[i][j])
                else:
                    arr[grid[i][j]-1]=True
        for i in range(len(arr)):
            if not(arr[i]):
                to_return.append(i+1)
        return to_return