class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        what i can think here is i will first search and find the row and col where the element is 0 and then from there  i  will move toward left and right
            1    1   1
            1    0   1
            1    1   1
            
            2nd row  and 2ndcol
            row will be constant col will be changing from 0 to upper bond
            matrix[][col]
            col will be constant and row will be changing from 0 to upper bond
            matrix 

            its a 0(n) to search 0th
            after that we are performing two pass
            that is keeping row as constant
            and keeping col as constant 
            both will be again 0 (m)
            o(n)
            o(n) * o (m + n)

        '''
        R = len(matrix)
        C = len(matrix[0])

        first_col = False
        for i in range(R):
            if matrix [i][0] == 0:
                first_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    # mark horizintal
                    matrix[i][0] = 0
                    # mark vertically
                    matrix[0][j] = 0
       
        # once we mark we do a linear traversal leaving the 0th row and col
        for i in range(1, R):
            for j in range(1, C):
                if ((matrix[i][0] == 0) or (matrix[0][j] == 0)):
                    matrix[i][j] = 0
        
        # Now lets check for the first row
        if matrix[0][0] == 0:
            for i in range(C):
                matrix[0][i] = 0
        # col
        if first_col:
            for i in range(R):
                matrix[i][0] = 0
        return matrix

            