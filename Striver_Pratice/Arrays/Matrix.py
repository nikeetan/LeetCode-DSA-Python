'''
Do all the rows and colums to be zero


A=[[1,1,1],[1,0,1],[1,1,1]]
[  1  1  1
   1  0  1
   1  1  1]

'''
class Matrix:
   def __init__(self,matrix):
      self.matrix=matrix
   def operation(self):
      #First Pass store the row and column index where there is 0
      row_indx=[]
      col_indx=[]
      row_size=len(self.matrix)
      col_size=len(self.matrix[0])
      for row in range(row_size):
         for col in range(col_size):
            if self.matrix[row][col]==0:
               row_indx.append(row)
               col_indx.append(col)
      #Second Pass
      #make the rows_indx, col_indx = 0
      for i in range(row_size):
         if i in row_indx:
            self.matrix[i]=[0]*col_size
         else:
            for j in range(col_size):
               if j in col_indx:
                  self.matrix[i][j]=0
      return self.matrix
   



#matrix_array=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix_array=[[1,1,1],[1,0,1],[1,1,1]]
Set_Matrix=Matrix(matrix_array)
print(Set_Matrix.operation())
   


