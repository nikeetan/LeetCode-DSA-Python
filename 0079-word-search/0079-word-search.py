class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        R, C = len(board), len(board[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(curr_row, curr_col , nxt_indx):

            if nxt_indx == len(word):
                return True

            for dirX, dirY in directions:

                nei_x = curr_row + dirX
                nei_y = curr_col + dirY

                if (0 <= nei_x < R) and (0 <= nei_y < C) and (board[nei_x][nei_y] == word[nxt_indx]):
                    temp = board[nei_x][nei_y]
                    print(temp)
                    board[nei_x][nei_y] = '#'
                    if dfs(nei_x, nei_y, nxt_indx + 1):
                        print(" i am here", word[nxt_indx], nei_x, nei_y)
                        return True
                    board[nei_x][nei_y] = temp
            return False
     
        def find_start():
            for i in range(R):
                for j in range(C):
                    # found the start
                    if board[i][j] == word[0]:
                        temp = board[i][j]
                        board[i][j] = '#'
                        print(i , j)
                        if dfs(i , j, 1):
                            return True
                        board[i][j] = temp
            return False
        return find_start()
        

