class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        new_matrix = [row[::-1] for row in new_matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = new_matrix[i][j]


        