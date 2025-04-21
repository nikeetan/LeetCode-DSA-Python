class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        

        for i in range(len(matrix)):
            p1 , p2 = 0 , len(matrix[i]) - 1
            while p1 < p2:
                matrix[i][p1] , matrix[i][p2] = matrix[i][p2], matrix[i][p1]
                p1 += 1
                p2 -= 1



        