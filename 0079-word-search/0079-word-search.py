class Solution:
    def __init__(self):
        self.directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    def dfs(self , R, C, board, row, col, word, indx):
        if indx == len(word):
            return True
        for dir_x, dir_y in self.directions:
            new_row, new_col = row + dir_x, col + dir_y
            if ((0 <= new_row <R) and (0 <= new_col < C)):
                if board[new_row][new_col] == word[indx]:
                    temp = board[new_row][new_col]
                    board[new_row][new_col] = '#'
                    if self.dfs(R, C, board, new_row, new_col, word, indx + 1):
                        return True
                    board[new_row][new_col] = temp
        return False

    def exist(self,board: list[list[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        indx = 0
        for row in range(R):
            for col in range(C):
                if board[row][col] == word[indx]:
                    temp = board[row][col]
                    board[row][col] = '#'
                    if self.dfs(R, C, board, row, col, word, indx + 1):
                        return True
                    board[row][col] = temp
        return False
        

