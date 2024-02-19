import re
board=[[".",".","4",".",".",".","6","3","."],
       [".",".",".",".",".",".",".",".","."],
       ["5",".",".",".",".",".",".","9","."],
       [".",".",".","5","6",".",".",".","."],
       ["4",".","3",".",".",".",".",".","1"],
       [".",".",".","7",".",".",".",".","."],
       [".",".",".","5",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]

no_of_rows,no_of_columns=len(board),len(board[0])
pattern="[\d+$]"

#checking for Row

def check_row(board):
    for i in range(no_of_rows):
        k=""
        for j in range(no_of_columns):
            k=k+board[i][j]
        j1=re.findall(pattern,k)
        l=set(j1)
        if len(j1)!=len(l):
            return False
    return True
                   

#Checking for Column 
def check_col(board):
    for i in range(no_of_columns):
        k=""
        for j in range(no_of_rows):
            k=k+board[j][i]
        j1=re.findall(pattern,k)
        l=set(j1)

        if len(j1)!=len(l):
            # print("I am here")
            # print(j1,l)
            return False
    return True


#Checking for 3X3
def traversing(board,row_size,column_size,start_index_row,start_index_col):
    k=""
    for i in range(start_index_row,row_size):
        for j in range(start_index_col,column_size):
            k=k+board[i][j]
    j=re.findall(pattern,k)
    l=set(j)
    if len(j)!=len(l):
        return False
    
def defining_size():
    row_size=3
    column_size=3
    start_index_row=0
    start_index_col=0
    
    var1=check_row(board)
    if var1==False:
        return False
    var2=check_col(board)
    if var2==False:
        return False    

    while(row_size<=no_of_rows):
        print("Hi I went here")
        if column_size<=no_of_columns:
            k1=traversing(board,row_size,column_size,start_index_row,start_index_col)
            if k1==False:
                return False
            else:
                start_index_col+=3
                column_size+=3
            
        else:
            start_index_row+=3
            start_index_col=0
            row_size+=3
            column_size=3
    return True

print(defining_size())
