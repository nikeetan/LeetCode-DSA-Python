class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x=[[ [] for i in range(len(matrix))]for j in range(len(matrix[0]))]
        rows,cols=len(matrix),len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                x[j][i]=matrix[i][j]
    
        return x