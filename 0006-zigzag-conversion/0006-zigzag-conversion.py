class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Thinking in the form of matrix
        '''
        matrix=[['1']for i in range(numRows)]
        pointer=0
        cols=0
        while pointer<len(s):
            for i in range(numRows):
                while len(matrix[i])!=cols+1:
                    matrix[i].append([])
                if pointer<len(s):
                    matrix[i][cols]=s[pointer]
                pointer+=1
            cols+=1
            for j in range(i-1,0,-1):
                while len(matrix[j])!=cols+1:
                    matrix[j].append([])
                if pointer<len(s):
                    matrix[j][cols]=s[pointer]
                pointer+=1
                cols+=1
        to_return=""
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j]!='1') and len(matrix[i][j])!=0:
                        to_return+=(matrix[i][j])
        return to_return
        
