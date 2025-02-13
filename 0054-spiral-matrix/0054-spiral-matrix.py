class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,left=0,0
        bottom,right=len(matrix)-1,len(matrix[0])-1
        to_return=[]

        while top<=bottom and left<=right:
            print(top,bottom,left,right)
            print(to_return)
            for i in range(left,right+1):
                to_return.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                to_return.append(matrix[j][right])
            print(to_return)
            right-=1
            if right>=left and top<=bottom:
                for j in range(right,left-1,-1):
                    to_return.append(matrix[bottom][j])
                bottom-=1
                for j in range(bottom,top-1,-1):
                    to_return.append(matrix[j][left])
                left+=1           
        return to_return


            
            

