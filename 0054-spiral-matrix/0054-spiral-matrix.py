'''
top = 0 left = 0                    right = len(rows[0])


edge cases where in i have 1 single row
0  1   2
top += 1 

if top< bottom:
    then only we will proceed

top = 0 
left = 0

9

8

7

# Traverse will be left to right and after that from top to bottom we will check
right -= 1
if left <= right:
else breal

bottom = len(matrix)

left  right top bottom right - 
1  2  
check top < bottom
from right we will traverse till bottom - 
3  6   

right -= 1

if left < right


'''

class Solution:

    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left , right = 0 , len(matrix[0]) # left = 0 right = 3
        top , bottom = 0 , len(matrix)  # top = 0 bottom = 3
        res = []                        # []
        
        ## Traversal
        while top < bottom and left < right:  
            
            ## Traversing from left to right
            for i in range(left , right):   
                res.append(matrix[left][i])     
            top += 1                              
            if top >= bottom:
                break
            ## Traversing fro top to bottom.
            for j in range(top , bottom):
                res.append( matrix[j][right - 1])     
            right -= 1                          
            if left >= right:                   
                break
            ## Traverse right to left               
            for k in range (right - 1, left, - 1):
                res.append(matrix[bottom - 1][k])   
            bottom -= 1                         

            ## Traverse from bottom to top
            for l in range(bottom, top - 1, -1):       
                res.append(matrix[l][left])     
            left += 1                           
        return res

            


