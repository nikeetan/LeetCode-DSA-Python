class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix=[[] for x in range(len(matrix[0]))]
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                new_matrix[j].append(matrix[i][j])
        return new_matrix