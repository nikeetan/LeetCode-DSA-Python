class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:


    #     R, C = len(board), len(board[0])
    #     directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    #     def dfs(curr_row, curr_col , nxt_indx):

    #         if nxt_indx == len(word):
    #             return True

    #         for dirX, dirY in directions:

    #             nei_x = curr_row + dirX
    #             nei_y = curr_col + dirY

    #             if (0 <= nei_x < R) and (0 <= nei_y < C) and (board[nei_x][nei_y] == word[nxt_indx]):
    #                 temp = board[nei_x][nei_y]
    #                 board[nei_x][nei_y] = '#'
    #                 if dfs(nei_x, nei_y, nxt_indx + 1):
    #                     return True
    #                 board[nei_x][nei_y] = temp
    #         return False
     
    #     def find_start():
    #         for i in range(R):
    #             for j in range(C):
    #                 # found the start
    #                 if board[i][j] == word[0]:
    #                     temp = board[i][j]
    #                     board[i][j] = '#'
    #                     if dfs(i , j, 1):
    #                         return True
    #                     board[i][j] = temp
    #         return False
    #     return find_start()
    def dfs(self , R, C, board, row, col, word, indx):
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def helper(indx, row, col):
            if indx == len(word):
                return True
            for dir_x, dir_y in directions:
                new_row, new_col = row + dir_x, col + dir_y
                if ((0 <= new_row <R) and (0 <= new_col < C)):
                    if board[new_row][new_col] == word[indx]:
                        temp = board[new_row][new_col]
                        board[new_row][new_col] = '#'
                        if helper(indx + 1, new_row, new_col):
                            return True
                        board[new_row][new_col] = temp
            return False
        return helper(indx + 1, row, col)




    def exist(self,board: list[list[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        indx = 0
        for row in range(R):
            for col in range(C):
                if board[row][col] == word[indx]:
                    temp = board[row][col]
                    board[row][col] = '#'
                    if self.dfs(R, C, board, row, col, word, indx):
                        return True
                    board[row][col] = temp
        return False
        

